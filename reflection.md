# Reflection – Lab 5: Static Code Analysis

## 1. Which issues were easiest and hardest to fix?
The easiest issues to fix were the **style-related** ones from Flake8 and Pylint, such as missing blank lines, invalid naming conventions, and unused imports.  
The hardest issues were the **security-related** ones — specifically removing the use of `eval()` and fixing the **mutable default argument** (`logs=[]`).  
These required understanding how Python handles memory, function defaults, and the risks of arbitrary code execution.

---

## 2. Were there any false positives?
Yes. Some warnings like **missing docstrings** for small helper functions were not truly critical for this short script.  
However, adding them still improved readability and overall Pylint score.

---

## 3. How would you integrate static analysis tools into a real project?
In a real software development workflow, I would integrate **Pylint**, **Flake8**, and **Bandit** using:
- **Pre-commit hooks** (to automatically scan before committing)
- **GitHub Actions or CI/CD pipelines** (to run checks on every pull request)
This ensures consistent code quality and prevents insecure or poorly formatted code from entering production.

---

## 4. What improvements did you notice after applying fixes?
After applying all the fixes:
- Code readability and maintainability improved significantly.  
- Security issues were eliminated (no `eval()`, no bare `except`).  
- File handling became safer with `with open(..., encoding="utf-8")`.  
- The program is now **PEP 8 compliant** and the **Pylint score improved from 4.8 → 9.25/10**.  
- Overall, static analysis made the code more professional, secure, and production-ready.
