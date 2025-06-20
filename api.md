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
    ProjectInviteSmeResponse,
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
- <code title="get /api/projects/{project_id}/export">client.projects.<a href="./src/codex/resources/projects/projects.py">export</a>(project_id) -> object</code>
- <code title="post /api/projects/{project_id}/increment_queries">client.projects.<a href="./src/codex/resources/projects/projects.py">increment_queries</a>(project_id, \*\*<a href="src/codex/types/project_increment_queries_params.py">params</a>) -> object</code>
- <code title="post /api/projects/{project_id}/notifications">client.projects.<a href="./src/codex/resources/projects/projects.py">invite_sme</a>(project_id, \*\*<a href="src/codex/types/project_invite_sme_params.py">params</a>) -> <a href="./src/codex/types/project_invite_sme_response.py">ProjectInviteSmeResponse</a></code>
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

## Evals

Types:

```python
from codex.types.projects import EvalListResponse
```

Methods:

- <code title="post /api/projects/{project_id}/evals">client.projects.evals.<a href="./src/codex/resources/projects/evals.py">create</a>(project_id, \*\*<a href="src/codex/types/projects/eval_create_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="put /api/projects/{project_id}/evals/{eval_key}">client.projects.evals.<a href="./src/codex/resources/projects/evals.py">update</a>(path_eval_key, \*, project_id, \*\*<a href="src/codex/types/projects/eval_update_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="get /api/projects/{project_id}/evals">client.projects.evals.<a href="./src/codex/resources/projects/evals.py">list</a>(project_id) -> <a href="./src/codex/types/projects/eval_list_response.py">EvalListResponse</a></code>
- <code title="delete /api/projects/{project_id}/evals/{eval_key}">client.projects.evals.<a href="./src/codex/resources/projects/evals.py">delete</a>(eval_key, \*, project_id) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>

## QueryLogs

Types:

```python
from codex.types.projects import (
    QueryLogRetrieveResponse,
    QueryLogListResponse,
    QueryLogListByGroupResponse,
    QueryLogListGroupsResponse,
    QueryLogStartRemediationResponse,
)
```

Methods:

- <code title="get /api/projects/{project_id}/query_logs/{query_log_id}">client.projects.query_logs.<a href="./src/codex/resources/projects/query_logs.py">retrieve</a>(query_log_id, \*, project_id) -> <a href="./src/codex/types/projects/query_log_retrieve_response.py">QueryLogRetrieveResponse</a></code>
- <code title="get /api/projects/{project_id}/query_logs/">client.projects.query_logs.<a href="./src/codex/resources/projects/query_logs.py">list</a>(project_id, \*\*<a href="src/codex/types/projects/query_log_list_params.py">params</a>) -> <a href="./src/codex/types/projects/query_log_list_response.py">QueryLogListResponse</a></code>
- <code title="get /api/projects/{project_id}/query_logs/logs_by_group">client.projects.query_logs.<a href="./src/codex/resources/projects/query_logs.py">list_by_group</a>(project_id, \*\*<a href="src/codex/types/projects/query_log_list_by_group_params.py">params</a>) -> <a href="./src/codex/types/projects/query_log_list_by_group_response.py">QueryLogListByGroupResponse</a></code>
- <code title="get /api/projects/{project_id}/query_logs/groups">client.projects.query_logs.<a href="./src/codex/resources/projects/query_logs.py">list_groups</a>(project_id, \*\*<a href="src/codex/types/projects/query_log_list_groups_params.py">params</a>) -> <a href="./src/codex/types/projects/query_log_list_groups_response.py">QueryLogListGroupsResponse</a></code>
- <code title="post /api/projects/{project_id}/query_logs/{query_log_id}/start_remediation">client.projects.query_logs.<a href="./src/codex/resources/projects/query_logs.py">start_remediation</a>(query_log_id, \*, project_id) -> <a href="./src/codex/types/projects/query_log_start_remediation_response.py">QueryLogStartRemediationResponse</a></code>

## Remediations

Types:

```python
from codex.types.projects import (
    RemediationCreateResponse,
    RemediationRetrieveResponse,
    RemediationListResponse,
    RemediationEditAnswerResponse,
    RemediationEditDraftAnswerResponse,
    RemediationGetResolvedLogsCountResponse,
    RemediationListResolvedLogsResponse,
    RemediationPauseResponse,
    RemediationPublishResponse,
    RemediationUnpauseResponse,
)
```

Methods:

- <code title="post /api/projects/{project_id}/remediations/">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">create</a>(project_id, \*\*<a href="src/codex/types/projects/remediation_create_params.py">params</a>) -> <a href="./src/codex/types/projects/remediation_create_response.py">RemediationCreateResponse</a></code>
- <code title="get /api/projects/{project_id}/remediations/{remediation_id}">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">retrieve</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_retrieve_response.py">RemediationRetrieveResponse</a></code>
- <code title="get /api/projects/{project_id}/remediations/">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">list</a>(project_id, \*\*<a href="src/codex/types/projects/remediation_list_params.py">params</a>) -> <a href="./src/codex/types/projects/remediation_list_response.py">RemediationListResponse</a></code>
- <code title="delete /api/projects/{project_id}/remediations/{remediation_id}">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">delete</a>(remediation_id, \*, project_id) -> None</code>
- <code title="patch /api/projects/{project_id}/remediations/{remediation_id}/edit_answer">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">edit_answer</a>(remediation_id, \*, project_id, \*\*<a href="src/codex/types/projects/remediation_edit_answer_params.py">params</a>) -> <a href="./src/codex/types/projects/remediation_edit_answer_response.py">RemediationEditAnswerResponse</a></code>
- <code title="patch /api/projects/{project_id}/remediations/{remediation_id}/edit_draft_answer">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">edit_draft_answer</a>(remediation_id, \*, project_id, \*\*<a href="src/codex/types/projects/remediation_edit_draft_answer_params.py">params</a>) -> <a href="./src/codex/types/projects/remediation_edit_draft_answer_response.py">RemediationEditDraftAnswerResponse</a></code>
- <code title="get /api/projects/{project_id}/remediations/{remediation_id}/resolved_logs_count">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">get_resolved_logs_count</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_get_resolved_logs_count_response.py">RemediationGetResolvedLogsCountResponse</a></code>
- <code title="get /api/projects/{project_id}/remediations/{remediation_id}/resolved_logs">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">list_resolved_logs</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_list_resolved_logs_response.py">RemediationListResolvedLogsResponse</a></code>
- <code title="patch /api/projects/{project_id}/remediations/{remediation_id}/pause">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">pause</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_pause_response.py">RemediationPauseResponse</a></code>
- <code title="patch /api/projects/{project_id}/remediations/{remediation_id}/publish">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">publish</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_publish_response.py">RemediationPublishResponse</a></code>
- <code title="patch /api/projects/{project_id}/remediations/{remediation_id}/unpause">client.projects.remediations.<a href="./src/codex/resources/projects/remediations.py">unpause</a>(remediation_id, \*, project_id) -> <a href="./src/codex/types/projects/remediation_unpause_response.py">RemediationUnpauseResponse</a></code>

# Tlm

Types:

```python
from codex.types import TlmPromptResponse, TlmScoreResponse
```

Methods:

- <code title="post /api/tlm/prompt">client.tlm.<a href="./src/codex/resources/tlm.py">prompt</a>(\*\*<a href="src/codex/types/tlm_prompt_params.py">params</a>) -> <a href="./src/codex/types/tlm_prompt_response.py">TlmPromptResponse</a></code>
- <code title="post /api/tlm/score">client.tlm.<a href="./src/codex/resources/tlm.py">score</a>(\*\*<a href="src/codex/types/tlm_score_params.py">params</a>) -> <a href="./src/codex/types/tlm_score_response.py">TlmScoreResponse</a></code>
