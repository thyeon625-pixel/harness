# External Service Policy

Default policy: **free-only, no protected-source upload, approval-required for credentials or paid APIs**.

## Default Decision Table

| Service/Tool Class | Default | Approval Needed When |
|---|---|---|
| public web search/fetch | allowed as research evidence | result affects identity/philosophy claims |
| GitHub public repo read | allowed | private repo/token/write access is needed |
| image generation | disabled by default | any external upload or paid generation is needed |
| Figma/Notion/Slack/Google APIs | disabled by default | auth token, workspace access, or write action is needed |
| OpenAI/Anthropic/Gemini API | approval-required unless already configured as free/no-extra-cost | cost or file upload may occur |
| local scripts | allowed inside run workspace | script modifies canonical files |

## Required Manifest Entry

Every run records:

```yaml
external_services:
  policy: none | free-only | approval-required
  used:
    - name: service-name
      purpose: why-used
      cost_risk: none | low | paid-risk
      protected_upload: false
      user_approval: not-needed | requested | approved
```

## Evidence Rule

External information may support Research World and market/trend analysis. It must not override user-authored Identity/Philosophy sources. If external research conflicts with internal DNA, report the conflict instead of resolving it silently.
