# Proof of Concept - Volunteer Shift Manager

## Deployment Readiness
- Web app + API routes active
- Container and PaaS deployment files included
- Automated test suite and CI workflow included

## Smoke Commands
```bash
python run.py
curl http://localhost:5000/api/health
curl http://localhost:5000/api/schema
curl -X POST http://localhost:5000/api/items   -H "Content-Type: application/json"   -d '{"title":"Phase3 Demo","status":"proposed","payload":{"host":"sample","participants":5,"community_notes":"notes"}}'
curl http://localhost:5000/api/metrics
```

## Metadata
- Generated UTC: 2026-03-24T16:15:12.141885+00:00
- Phase: 3
- Domain: Community
