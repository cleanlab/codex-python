# Health

Types:

```python
from codex.types import HealthCheckResponse
```

Methods:

- <code title="get /api/health/">client.health.<a href="./src/codex/resources/health.py">check</a>() -> <a href="./src/codex/types/health_check_response.py">HealthCheckResponse</a></code>
- <code title="get /api/health/db">client.health.<a href="./src/codex/resources/health.py">db</a>() -> <a href="./src/codex/types/health_check_response.py">HealthCheckResponse</a></code>

# Organizations

Types:

```python
from codex.types import (
    OrganizationSchemaPublic,
    OrganizationListMembersResponse,
    OrganizationRetrievePermissionsResponse,
)
```

Methods:

- <code title="get /api/organizations/{organization_id}">client.organizations.<a href="./src/codex/resources/organizations/organizations.py">retrieve</a>(organization_id) -> <a href="./src/codex/types/organization_schema_public.py">OrganizationSchemaPublic</a></code>
- <code title="get /api/organizations/{organization_id}/members">client.organizations.<a href="./src/codex/resources/organizations/organizations.py">list_members</a>(organization_id) -> <a href="./src/codex/types/organization_list_members_response.py">OrganizationListMembersResponse</a></code>
- <code title="get /api/organizations/{organization_id}/permissions">client.organizations.<a href="./src/codex/resources/organizations/organizations.py">retrieve_permissions</a>(organization_id) -> <a href="./src/codex/types/organization_retrieve_permissions_response.py">OrganizationRetrievePermissionsResponse</a></code>

## Billing

Types:

```python
from codex.types.organizations import (
    OrganizationBillingInvoicesSchema,
    OrganizationBillingUsageSchema,
)
```

Methods:

- <code title="get /api/organizations/{organization_id}/billing/invoices">client.organizations.billing.<a href="./src/codex/resources/organizations/billing/billing.py">invoices</a>(organization_id) -> <a href="./src/codex/types/organizations/organization_billing_invoices_schema.py">OrganizationBillingInvoicesSchema</a></code>
- <code title="get /api/organizations/{organization_id}/billing/usage">client.organizations.billing.<a href="./src/codex/resources/organizations/billing/billing.py">usage</a>(organization_id) -> <a href="./src/codex/types/organizations/organization_billing_usage_schema.py">OrganizationBillingUsageSchema</a></code>

### CardDetails

Types:

```python
from codex.types.organizations.billing import OrganizationBillingCardDetails
```

Methods:

- <code title="get /api/organizations/{organization_id}/billing/card-details">client.organizations.billing.card_details.<a href="./src/codex/resources/organizations/billing/card_details.py">retrieve</a>(organization_id) -> <a href="./src/codex/types/organizations/billing/organization_billing_card_details.py">Optional[OrganizationBillingCardDetails]</a></code>

### SetupIntent

Types:

```python
from codex.types.organizations.billing import OrganizationBillingSetupIntent
```

Methods:

- <code title="post /api/organizations/{organization_id}/billing/setup-intent">client.organizations.billing.setup_intent.<a href="./src/codex/resources/organizations/billing/setup_intent.py">create</a>(organization_id) -> <a href="./src/codex/types/organizations/billing/organization_billing_setup_intent.py">OrganizationBillingSetupIntent</a></code>

### PlanDetails

Types:

```python
from codex.types.organizations.billing import OrganizationBillingPlanDetails
```

Methods:

- <code title="get /api/organizations/{organization_id}/billing/plan-details">client.organizations.billing.plan_details.<a href="./src/codex/resources/organizations/billing/plan_details.py">retrieve</a>(organization_id) -> <a href="./src/codex/types/organizations/billing/organization_billing_plan_details.py">OrganizationBillingPlanDetails</a></code>

# Users

Methods:

- <code title="patch /api/users/activate_account">client.users.<a href="./src/codex/resources/users/users.py">activate_account</a>(\*\*<a href="src/codex/types/user_activate_account_params.py">params</a>) -> <a href="./src/codex/types/users/user_schema_public.py">UserSchemaPublic</a></code>

## Myself

Types:

```python
from codex.types.users import UserSchema, UserSchemaPublic
```

Methods:

- <code title="get /api/users/myself">client.users.myself.<a href="./src/codex/resources/users/myself/myself.py">retrieve</a>() -> <a href="./src/codex/types/users/user_schema_public.py">UserSchemaPublic</a></code>

### APIKey

Methods:

- <code title="get /api/users/myself/api-key">client.users.myself.api_key.<a href="./src/codex/resources/users/myself/api_key.py">retrieve</a>() -> <a href="./src/codex/types/users/user_schema_public.py">UserSchemaPublic</a></code>
- <code title="post /api/users/myself/api-key/refresh">client.users.myself.api_key.<a href="./src/codex/resources/users/myself/api_key.py">refresh</a>() -> <a href="./src/codex/types/users/user_schema.py">UserSchema</a></code>

### Organizations

Types:

```python
from codex.types.users.myself import UserOrganizationsSchema
```

Methods:

- <code title="get /api/users/myself/organizations">client.users.myself.organizations.<a href="./src/codex/resources/users/myself/organizations.py">list</a>() -> <a href="./src/codex/types/users/myself/user_organizations_schema.py">UserOrganizationsSchema</a></code>

## Verification

Types:

```python
from codex.types.users import VerificationResendResponse
```

Methods:

- <code title="post /api/users/verification/resend">client.users.verification.<a href="./src/codex/resources/users/verification.py">resend</a>() -> <a href="./src/codex/types/users/verification_resend_response.py">VerificationResendResponse</a></code>

# Projects

Types:

```python
from codex.types import (
    ProjectReturnSchema,
    ProjectRetrieveResponse,
    ProjectListResponse,
    ProjectExportResponse,
    ProjectIncrementQueriesResponse,
    ProjectRetrieveAnalyticsResponse,
    ProjectValidateResponse,
)
```

Methods:

- <code title="post /api/projects/">client.projects.<a href="./src/codex/resources/projects/projects.py">create</a>(\*\*<a href="src/codex/types/project_create_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="get /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/codex/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="put /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/codex/types/project_update_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="get /api/projects/">client.projects.<a href="./src/codex/resources/projects/projects.py">list</a>(\*\*<a href="src/codex/types/project_list_params.py">params</a>) -> <a href="./src/codex/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="get /api/projects/{project_id}/export">client.projects.<a href="./src/codex/resources/projects/projects.py">export</a>(project_id) -> <a href="./src/codex/types/project_export_response.py">object</a></code>
- <code title="post /api/projects/{project_id}/increment_queries">client.projects.<a href="./src/codex/resources/projects/projects.py">increment_queries</a>(project_id, \*\*<a href="src/codex/types/project_increment_queries_params.py">params</a>) -> <a href="./src/codex/types/project_increment_queries_response.py">object</a></code>
- <code title="get /api/projects/{project_id}/analytics/">client.projects.<a href="./src/codex/resources/projects/projects.py">retrieve_analytics</a>(project_id, \*\*<a href="src/codex/types/project_retrieve_analytics_params.py">params</a>) -> <a href="./src/codex/types/project_retrieve_analytics_response.py">ProjectRetrieveAnalyticsResponse</a></code>
- <code title="post /api/projects/{project_id}/validate">client.projects.<a href="./src/codex/resources/projects/projects.py">validate</a>(project_id, \*\*<a href="src/codex/types/project_validate_params.py">params</a>) -> <a href="./src/codex/types/project_validate_response.py">ProjectValidateResponse</a></code>

## AccessKeys

Types:

```python
from codex.types.projects import (
    AccessKeySchema,
    AccessKeyListResponse,
    AccessKeyRetrieveProjectIDResponse,
)
```

Methods:

- <code title="post /api/projects/{project_id}/access_keys/">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">create</a>(project_id, \*\*<a href="src/codex/types/projects/access_key_create_params.py">params</a>) -> <a href="./src/codex/types/projects/access_key_schema.py">AccessKeySchema</a></code>
- <code title="get /api/projects/{project_id}/access_keys/{access_key_id}">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">retrieve</a>(access_key_id, \*, project_id) -> <a href="./src/codex/types/projects/access_key_schema.py">AccessKeySchema</a></code>
- <code title="put /api/projects/{project_id}/access_keys/{access_key_id}">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">update</a>(access_key_id, \*, project_id, \*\*<a href="src/codex/types/projects/access_key_update_params.py">params</a>) -> <a href="./src/codex/types/projects/access_key_schema.py">AccessKeySchema</a></code>
- <code title="get /api/projects/{project_id}/access_keys/">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">list</a>(project_id) -> <a href="./src/codex/types/projects/access_key_list_response.py">AccessKeyListResponse</a></code>
- <code title="delete /api/projects/{project_id}/access_keys/{access_key_id}">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">delete</a>(access_key_id, \*, project_id) -> None</code>
- <code title="get /api/projects/id_from_access_key">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">retrieve_project_id</a>() -> <a href="./src/codex/types/projects/access_key_retrieve_project_id_response.py">AccessKeyRetrieveProjectIDResponse</a></code>
- <code title="post /api/projects/{project_id}/access_keys/{access_key_id}/revoke">client.projects.access_keys.<a href="./src/codex/resources/projects/access_keys.py">revoke</a>(access_key_id, \*, project_id) -> None</code>

## Entries

Types:

```python
from codex.types.projects import Entry, EntryNotifySmeResponse, EntryQueryResponse
```

Methods:

- <code title="post /api/projects/{project_id}/entries/">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">create</a>(project_id, \*\*<a href="src/codex/types/projects/entry_create_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="get /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">retrieve</a>(entry_id, \*, project_id) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="put /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">update</a>(entry_id, \*, project_id, \*\*<a href="src/codex/types/projects/entry_update_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="delete /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">delete</a>(entry_id, \*, project_id) -> None</code>
- <code title="post /api/projects/{project_id}/entries/{entry_id}/notifications">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">notify_sme</a>(entry_id, \*, project_id, \*\*<a href="src/codex/types/projects/entry_notify_sme_params.py">params</a>) -> <a href="./src/codex/types/projects/entry_notify_sme_response.py">EntryNotifySmeResponse</a></code>
- <code title="put /api/projects/{project_id}/entries/{entry_id}/publish_draft_answer">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">publish_draft_answer</a>(entry_id, \*, project_id) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="post /api/projects/{project_id}/entries/query">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">query</a>(project_id, \*\*<a href="src/codex/types/projects/entry_query_params.py">params</a>) -> <a href="./src/codex/types/projects/entry_query_response.py">EntryQueryResponse</a></code>
- <code title="put /api/projects/{project_id}/entries/{entry_id}/unpublish_answer">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">unpublish_answer</a>(entry_id, \*, project_id) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>

## Clusters

Types:

```python
from codex.types.projects import ClusterListResponse, ClusterListVariantsResponse
```

Methods:

- <code title="get /api/projects/{project_id}/entries/clusters">client.projects.clusters.<a href="./src/codex/resources/projects/clusters.py">list</a>(project_id, \*\*<a href="src/codex/types/projects/cluster_list_params.py">params</a>) -> <a href="./src/codex/types/projects/cluster_list_response.py">SyncOffsetPageClusters[ClusterListResponse]</a></code>
- <code title="get /api/projects/{project_id}/entries/clusters/{representative_entry_id}">client.projects.clusters.<a href="./src/codex/resources/projects/clusters.py">list_variants</a>(representative_entry_id, \*, project_id) -> <a href="./src/codex/types/projects/cluster_list_variants_response.py">ClusterListVariantsResponse</a></code>

# Tlm

Types:

```python
from codex.types import TlmPromptResponse, TlmScoreResponse
```

Methods:

- <code title="post /api/tlm/prompt">client.tlm.<a href="./src/codex/resources/tlm.py">prompt</a>(\*\*<a href="src/codex/types/tlm_prompt_params.py">params</a>) -> <a href="./src/codex/types/tlm_prompt_response.py">TlmPromptResponse</a></code>
- <code title="post /api/tlm/score">client.tlm.<a href="./src/codex/resources/tlm.py">score</a>(\*\*<a href="src/codex/types/tlm_score_params.py">params</a>) -> <a href="./src/codex/types/tlm_score_response.py">TlmScoreResponse</a></code>
