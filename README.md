# python-security-lab-demo

This repository is part of a cybersecurity lab exercise demonstrating **GitHub Security features** such as **Dependabot** and **Bandit** for Python projects.

The purpose of this lab is to intentionally include insecure code and dependencies, analyze the results using automated security tools, and then apply remediations to fix the detected issues.

## 🧠 Objectives
- Create a GitHub repository with intentionally vulnerable Python code.
- Enable **Dependabot** to detect vulnerable dependencies.
- Run **Bandit** (Python static analyzer) to identify security flaws in source code.
- Review the generated alerts and apply recommended fixes.
- Re-run the tools to confirm that vulnerabilities have been resolved.

## ⚙️ Tools Used
- **GitHub Dependabot** — Scans dependencies for known vulnerabilities.
- **Bandit** — Detects insecure coding practices in Python source files.
- **GitHub Code Scanning** — Displays alerts and tracks resolutions.

## 📁 Files
- `main.py` – Vulnerable and later fixed Python script used for testing.
- `requirements.txt` – Contains a vulnerable version of `PyYAML` for Dependabot testing.
- `config.yaml` – Sample input configuration file used by the script.

## 🧩 Summary
This project demonstrates how automated security analysis can help developers find and fix vulnerabilities early in the software development process. It highlights the importance of secure coding practices and dependency management within DevSecOps workflows.
