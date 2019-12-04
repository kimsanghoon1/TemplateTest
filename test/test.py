forEach: BoundedContext
fileName: {{name}}World.py
path: {{name}}
---
print("BoundedContext: {{name}}");
{{#aggregates}}
print("Aggregate: {{name}}");
{{#events}}
print("event: {{name}}");
{{/events}}
{{#commands}}
print("command: {{name}}");
{{/commands}}
{{#policies}}
print("policy: {{name}}");
{{/policies}}
{{/aggregates}}
