# Data Snapshots

Machine-readable dated snapshots of authorization state for
managed-service vendors cited in the cmmc-advisor corpus. The
snapshots are agent-facing reference data: they reduce network
dependency at advice time and centralize the verification date
that corpus prose files hedge to.

## Files

- **fedramp-snapshot.json** — FedRAMP authorization state for the
  six productivity-corpus vendors (Microsoft 365 GCC, Microsoft
  365 GCC High, Google Workspace + Assured Controls Plus,
  Atlassian Government Cloud, ServiceNow GCC, GitHub Enterprise
  Cloud, Box for Government) plus the three AI-service vendors
  (Amazon Bedrock GovCloud, Azure OpenAI Government, Vertex AI
  Assured Workloads). Ten entries total.

## What the snapshot is

A starting reference for agent-grounded responses that need
authorization-state facts. Each entry carries:

- `id` — stable identifier
- `product` — vendor-facing product name
- `vendor` — parent vendor
- `fedramp_impact_level` — Low / Moderate / High / Tailored
- `dod_impact_level` — array of applicable IL authorizations
- `authorization_type` — P-ATO, JAB P-ATO, Agency ATO, Tailored
- `package_hint` — hint for finding the Marketplace package
- `cui_suitability` — short phrase on DFARS 7012 fit
- `primary_source` — authoritative URLs for verification
- `corpus_references` — which cmmc-advisor files cite this vendor
- `notes` — caveats, model-level availability, common miscitations

## What the snapshot is not

- **Not an SSP citation substitute.** Every authorization claim in
  an SSP should cite the current FedRAMP Marketplace package at
  marketplace.fedramp.gov with a live-verification date. This
  snapshot is a convenience reference, not an authoritative
  compliance record.
- **Not a complete catalog.** The FedRAMP Marketplace lists
  hundreds of authorized products across many capability
  categories. This snapshot scopes to the vendors the cmmc-advisor
  corpus references directly. Other authorized products exist and
  are fit for other contractor needs.
- **Not real-time.** The snapshot carries a `verification_date`
  field at the root and per-vendor notes with dates. Authorization
  state changes weekly; the snapshot drifts.

## Refresh cadence and mechanics

**Cadence:** refresh on each corpus review cycle, whenever a
vendor announces a tier-level change (new IL authorization, new
FedRAMP-tier upgrade, new Assured Workloads region), or quarterly
at minimum.

**Process (manual at the 2026-04-21 authoring):**

1. Open marketplace.fedramp.gov, search each vendor by name,
   capture the current FedRAMP Marketplace package entry details
   (impact level, authorization type, status).
2. Open each vendor's compliance or trust center page and confirm
   DoD IL overlays, CUI-suitability framing, and any recent
   announcements.
3. Update the JSON entry with the current state, bumping the root
   `verification_date` to the refresh date.
4. For each vendor whose state changed materially, update the
   corresponding corpus file prose with the new dated stamp and
   reference this snapshot for the machine-readable record.

**Automation follow-up:** the FedRAMP Marketplace exposes a JSON
endpoint (observable via browser devtools on marketplace.fedramp.gov;
not publicly documented). A scheduled task scraping that endpoint
plus each vendor's trust page could reduce the refresh process to
a diff-and-review step. Scoping this automation is a separate
task; the manual process above is the current reality.

## Schema

See `fedramp-snapshot.json` root field `schema_version` (currently
"1.0"). Field semantics in the "What the snapshot is" section
above. Backward-compatibility is not promised across schema
version bumps; consumers should check the version before parsing.

## Contributing

Updates to this snapshot follow the CONTRIBUTING.md provenance
rules: every authorization claim traces to a primary source
listed in the entry's `primary_source` field. Vendor-marketing
claims without a Marketplace package entry are not snapshot-
worthy; wait for the authoritative source.

When adding a new vendor entry, follow the existing entry shape
and include `corpus_references` pointing at the files that cite
the vendor. When removing a vendor (decommissioned product,
retired authorization), preserve the entry with an explicit
`status: retired` note rather than deleting — downstream
consumers may rely on the identifier persisting.
