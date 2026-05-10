# TDR Football Analysis - Contributing Guide

## 🤝 How to Contribute

### Setup Development

```bash
git clone https://github.com/otjunca859-ai/tdr-football-analysis.git
cd tdr-football-analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run Tests

```bash
streamlit run app.py
```

### File Structure

```
core/
  data_loader.py      - Data generation & loading
  metrics.py          - xG, correlations, normalizations
  analysis.py         - Conclusions, anomalies
  tactics.py          - Formations & recommendations
  storage.py          - Board persistence

pages/
  1_PreMatch_Report.py         - Team comparison & recommendations
  2_PostMatch_Evaluation.py    - Incident flags & model break
  3_Hypotheses.py              - H1/H2/H4 validation
  4_Tactical_Board.py          - Interactive board (canvas)
  5_Data_Sources_And_Licenses.py - Compliance & citations
```

## 📝 Code Style

- Follow PEP 8
- Use type hints where possible
- Comment functions with docstrings
- Use Streamlit best practices (caching with @st.cache_data)

## 🐛 Bug Reports

- Open GitHub Issue
- Include error message + steps to reproduce
- Attach streamlit version + Python version

## 🎯 Feature Requests

- Open GitHub Discussion
- Describe use case + expected behavior
- Reference hypothesis or page if applicable

## 📚 Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md for all changes
- Add docstrings for new functions

## 🔬 Testing Checklist

- [ ] All 5 pages load without errors
- [ ] Demo data generates correctly
- [ ] Metrics calculate properly
- [ ] Conclusions auto-generate
- [ ] Board saves/loads correctly
- [ ] Works 100% offline
- [ ] No console errors

## License

All contributions under MIT License.
