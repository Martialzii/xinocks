# Branch Plan Blueprint

## Concept
Create a new branch that evolves the current marketplace into a flexible build idea for future plan-source variations, combining the existing market experience with modular, extensible planning logic.

## Goals
- Preserve the current marketplace foundation.
- Introduce a configurable planning layer for multiple future sources and variants.
- Keep the experience extensible for new product, plan, and content variations.

## Proposed Modules
- Market Core: existing storefront and subscription flow.
- Plan Variations Engine: configurable strategy layer for future plan sources.
- Build Metadata: environment and build descriptors for inspector/debug workflows.
- Source Abstraction: a simple interface for switching between plan sources.

## Suggested Branch Direction
1. Keep existing Django market features intact.
2. Add an abstraction for plan/data sources.
3. Expose a lightweight API endpoint for plan variants.
4. Support future extension without breaking the current market flow.

## Repo Work Target: Build Foundation Projects
This branch should act as a foundation for future build-oriented repo work by organizing the current marketplace into reusable building blocks.

### Target Areas
- Market foundation: preserve the storefront and subscription experience.
- Build foundation: create reusable modules for plan variants and future expansion.
- Project scaffolding: make the repo easier to extend for new product builds.
- Workstream organization: separate core market logic from experimental build logic.

### Suggested Milestones
1. Stabilize the current market and agent server setup.
2. Introduce a simple source/plan abstraction for future builds.
3. Add a lightweight API or payload model for repo work targets.
4. Document how new build projects can be added without disrupting the existing flow.

### Deep Build Printblue Mode Features
This mode should provide a richer blueprint for future builds by mapping concepts into a print-friendly, feature-oriented structure.

- Feature concepts: adaptation, reasoning, resilience, user-choice, and token-aware response handling.
- Printblue mode: a clear, structured output view for concepts and build targets.
- Build layering: core market flow, plan abstraction, and future feature expansion remain separate.
- User-facing clarity: each build feature can be summarized in an easy-to-read format.

## Example Payload
```json
{
  "market": "xinocks",
  "plan_mode": "future_variations",
  "sources": ["market", "future-plans", "experimental"],
  "status": "ready"
}
```
