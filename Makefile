.PHONY: validate build clean

validate:
	python3 scripts/validate_data.py

build: validate
	python3 scripts/build_resume.py

clean:
	rm -f output/*.docx output/*.pdf
	rm -rf _build
