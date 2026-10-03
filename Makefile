.PHONY: validate build pdf clean

validate:
	uv run python scripts/validate_data.py

build: validate
	uv run python scripts/build_resume.py

pdf: validate
	uv run python scripts/build_resume.py --require-pdf

clean:
	rm -f output/*.docx output/*.pdf
	rm -rf _build
