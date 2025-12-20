.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest coverage gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and an HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub file"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  latexpdfnewly  to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual (man page) files"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to make a link-checking output"
	@echo "  doctest    to make doctest files"
	@echo "  coverage   to make a coverage report"
	@echo "  gettext    to make PO message catalogs"

clean:
	rm -rf _build/*

html:
	sphinx-build -b html -d _build/doctrees . _build/html

dirhtml:
	sphinx-build -b dirhtml -d _build/doctrees . _build/dirhtml

singlehtml:
	sphinx-build -b singlehtml -d _build/doctrees . _build/singlehtml

pickle:
	sphinx-build -b pickle -d _build/doctrees . _build/pickle

json:
	sphinx-build -b json -d _build/doctrees . _build/json

htmlhelp:
	sphinx-build -b htmlhelp -d _build/doctrees . _build/htmlhelp

qthelp:
	sphinx-build -b qthelp -d _build/doctrees . _build/qthelp

devhelp:
	sphinx-build -b devhelp -d _build/doctrees . _build/devhelp

epub:
	sphinx-build -b epub -d _build/doctrees . _build/epub

latex:
	sphinx-build -b latex -d _build/doctrees . _build/latex

latexpdf:
	sphinx-build -b latex -d _build/doctrees . _build/latex
	cd _build/latex && make all-pdf

text:
	sphinx-build -b text -d _build/doctrees . _build/text

man:
	sphinx-build -b man -d _build/doctrees . _build/man

changes:
	sphinx-build -b changes -d _build/doctrees . _build/changes

linkcheck:
	sphinx-build -b linkcheck -d _build/doctrees . _build/linkcheck

doctest:
	sphinx-build -b doctest -d _build/doctrees . _build/doctest

coverage:
	sphinx-build -b coverage -d _build/doctrees . _build/coverage

gettext:
	sphinx-build -b gettext -d _build/doctrees . _build/gettext
