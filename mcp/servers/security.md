# MCP servers — Security

Application security, secrets, threat intel, and cloud security posture. ⭐ = company-maintained.

| Server | Repo | Install |
|--------|------|---------|
| Semgrep ⭐ (SAST) | [semgrep/mcp](https://github.com/semgrep/mcp) | `uvx semgrep-mcp` |
| Snyk ⭐ | [snyk/snyk-ls](https://github.com/snyk/snyk-ls) | see repo |
| GitGuardian (secrets) | [GitGuardian/gg-mcp](https://github.com/GitGuardian/gg-shield) | see repo |
| Trivy (containers/IaC) | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | see repo |
| OSV / vuln lookup | [google/osv-scanner](https://github.com/google/osv-scanner) | see repo |
| BloodHound (AD attack paths) | [SpecterOps/BloodHound-MCP](https://github.com/MorDavid/BloodHound-MCP-AI) | see repo |
| Shodan | [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) | `npx -y mcp-shodan` |
| VirusTotal | [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) | `npx -y mcp-virustotal` |
| Cycode ⭐ (ASPM) | [cycodehq/cycode-cli](https://github.com/cycodehq/cycode-cli) | see repo |
| RAD Security ⭐ | [rad-security/mcp-server](https://github.com/rad-security/mcp-server) | see repo |
| Nuclei / ProjectDiscovery | [pd-actions](https://github.com/projectdiscovery) | see repo |
| urlDNA ⭐ | [urldna](https://urldna.io/) | see repo |

> Security tooling can be dual-use. Only run these against systems you're authorized to test, and
> review what data each server sends off-box.
