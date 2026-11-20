# Codex image API network access

Codex tool commands execute inside the sandbox selected by Easel. Successful
host DNS resolution or an offline image configuration check does not prove
that the sandbox can reach an image API. A network-disabled Linux sandbox can
report Temporary failure in name resolution even when host DNS works.

For a trusted project requiring external image generation, the administrator
can explicitly set EASEL_CODEX_NETWORK_ACCESS=true in the project environment.
Easel applies this opt-in to workspace-write turns only. The default remains
network-disabled; read-only policy, project writable roots and on-request
approval are unchanged. This enables outbound networking for workspace-write
commands generally, not just image generation; it is not a domain allowlist.
No global Codex configuration or operating system DNS change is required.

After installing the code change, the existing Web Python process must be
reloaded in a maintenance window to import the updated adapter. Subsequent
turns read the project environment setting. This repair does not restart the
running Web service. A separately launched Codex CLI does not automatically
consume this Easel adapter setting.

An HTTP 503 model_not_found response from the provider is a separate upstream
availability or group-routing issue. Do not change the configured API key,
model or endpoint to conceal it, and do not automatically retry a potentially
billable image submission after an ambiguous timeout.
