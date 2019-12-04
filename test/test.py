forEach: BoundedContext
fileName: {{name}}World.py
path: {{boundedContext}}/{{{options.packagePath}}}
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
