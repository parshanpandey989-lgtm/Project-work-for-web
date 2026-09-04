#!/usr/bin/env python3
"""Repeatable structural/syntax checks for the RoadLens Australia static site."""
from __future__ import annotations
import json,re,subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
EXPECTED_PAGES={"index.html","dashboard.html","trends.html","states.html","road-users.html","demographics.html","risk-factors.html","explorer.html","about-data.html","about.html"}
class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__();self.lang=None;self.title=False;self.main=False;self.nav=False;self.h1=False;self.csp=False;self.links=[];self.images_without_alt=[];self.control_ids=set();self.label_fors=set();self.inline_script=False;self.inline_style=False;self.in_title=False
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=="html":self.lang=d.get("lang")
        elif tag=="title":self.in_title=True
        elif tag=="main":self.main=True
        elif tag=="nav":self.nav=True
        elif tag=="h1":self.h1=True
        elif tag=="meta" and d.get("http-equiv","").lower()=="content-security-policy":self.csp=True
        elif tag=="a" and d.get("href"):self.links.append(d["href"])
        elif tag=="img" and "alt" not in d:self.images_without_alt.append(d.get("src","<unknown>"))
        elif tag in {"input","select","textarea"} and d.get("id"):self.control_ids.add(d["id"])
        elif tag=="label" and d.get("for"):self.label_fors.add(d["for"])
        elif tag=="script" and not d.get("src"):self.inline_script=True
        if "style" in d:self.inline_style=True
    def handle_endtag(self,tag):
        if tag=="title":self.in_title=False
    def handle_data(self,data):
        if self.in_title and data.strip():self.title=True
def is_local_href(href):
    if href.startswith(("#","mailto:","tel:","javascript:")):return False
    parsed=urlparse(href);return not parsed.scheme and not parsed.netloc
def check(condition,message,failures):
    print(("PASS — " if condition else "FAIL — ")+message)
    if not condition:failures.append(message)
def main():
    failures=[];pages={p.name for p in ROOT.glob("*.html")};check(pages==EXPECTED_PAGES,"exactly the 10 required HTML pages are present",failures)
    for page_name in sorted(EXPECTED_PAGES):
        page=ROOT/page_name;parser=AuditParser();source=page.read_text(encoding="utf-8");parser.feed(source)
        check(parser.lang=="en-AU",f"{page_name}: lang=en-AU",failures);check(parser.title,f"{page_name}: non-empty title",failures);check(parser.main and parser.nav and parser.h1,f"{page_name}: semantic main/nav/h1 structure",failures);check(parser.csp,f"{page_name}: Content Security Policy present",failures);check(not parser.images_without_alt,f"{page_name}: images include alt text",failures)
        unlabeled=parser.control_ids-parser.label_fors
        if unlabeled:unlabeled={cid for cid in unlabeled if not re.search(rf'id=["\']{re.escape(cid)}["\'][^>]*(aria-label|aria-labelledby)=',source)}
        check(not unlabeled,f"{page_name}: identified form controls are labelled",failures);check(not parser.inline_script,f"{page_name}: no inline JavaScript",failures);check(not parser.inline_style,f"{page_name}: no inline style attributes",failures)
        broken=[]
        for href in parser.links:
            if not is_local_href(href):continue
            clean=href.split("#",1)[0].split("?",1)[0]
            if clean and not (page.parent/clean).resolve().exists():broken.append(href)
        check(not broken,f"{page_name}: local links resolve",failures)
    try:json.loads((ROOT/"data"/"roadlens-data.json").read_text(encoding="utf-8"));json_ok=True
    except Exception:json_ok=False
    check(json_ok,"roadlens-data.json parses as valid JSON",failures)
    node=subprocess.run(["node","--check",str(ROOT/"assets"/"app.js")],capture_output=True,text=True);check(node.returncode==0,"assets/app.js passes node --check",failures)
    css=(ROOT/"assets"/"styles.css").read_text(encoding="utf-8");check("@media" in css,"responsive CSS media queries are present",failures);check(":focus-visible" in css,"visible keyboard focus styles are present",failures);check("prefers-reduced-motion" in css,"reduced-motion handling is present",failures)
    print("\n"+("ALL CHECKS PASSED" if not failures else f"{len(failures)} CHECK(S) FAILED"));return 1 if failures else 0
if __name__=="__main__":raise SystemExit(main())
