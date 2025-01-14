# Health

Types:

```python
from codex.types import HealthCheckResponse
```

Methods:

- <code title="get /api/health/">client.health.<a href="./src/codex/resources/health.py">check</a>() -> <a href="./src/codex/types/health_check_response.py">HealthCheckResponse</a></code>
- <code title="get /api/health/db">client.health.<a href="./src/codex/resources/health.py">db</a>() -> <a href="./src/codex/types/health_check_response.py">HealthCheckResponse</a></code>
- <code title="get /api/health/weaviate">client.health.<a href="./src/codex/resources/health.py">weaviate</a>() -> <a href="./src/codex/types/health_check_response.py">HealthCheckResponse</a></code>

# Organizations

Types:

```python
from codex.types import OrganizationSchemaPublic
```

Methods:

- <code title="get /api/organizations/{organization_id}">client.organizations.<a href="./src/codex/resources/organizations/organizations.py">retrieve</a>(organization_id) -> <a href="./src/codex/types/organization_schema_public.py">OrganizationSchemaPublic</a></code>

## Billing

Types:

```python
from codex.types.organizations import (
    OrganizationBillingInvoicesSchema,
    OrganizationBillingUsageSchema,
)
```

Methods:

- <code title="get /api/organizations/{organization_id}/billing/invoices">client.organizations.billing.<a href="./src/codex/resources/organizations/billing.py">invoices</a>(organization_id) -> <a href="./src/codex/types/organizations/organization_billing_invoices_schema.py">OrganizationBillingInvoicesSchema</a></code>
- <code title="get /api/organizations/{organization_id}/billing/usage">client.organizations.billing.<a href="./src/codex/resources/organizations/billing.py">usage</a>(organization_id) -> <a href="./src/codex/types/organizations/organization_billing_usage_schema.py">OrganizationBillingUsageSchema</a></code>

# Users

## Myself

Types:

```python
from codex.types.users import UserSchema, UserSchemaPublic
```

Methods:

- <code title="get /api/users/myself">client.users.myself.<a href="./src/codex/resources/users/myself/myself.py">retrieve</a>() -> <a href="./src/codex/types/users/user_schema_public.py">UserSchemaPublic</a></code>

### APIKey

Methods:

- <code title="post /api/users/myself/api-key/refresh">client.users.myself.api_key.<a href="./src/codex/resources/users/myself/api_key.py">refresh</a>() -> <a href="./src/codex/types/users/user_schema.py">UserSchema</a></code>

### Organizations

Types:

```python
from codex.types.users.myself import UserOrganizationsSchema
```

Methods:

- <code title="get /api/users/myself/organizations">client.users.myself.organizations.<a href="./src/codex/resources/users/myself/organizations.py">list</a>() -> <a href="./src/codex/types/users/myself/user_organizations_schema.py">UserOrganizationsSchema</a></code>

# Projects

Types:

```python
from codex.types import ProjectReturnSchema, ProjectListResponse, ProjectExportResponse
```

Methods:

- <code title="post /api/projects/">client.projects.<a href="./src/codex/resources/projects/projects.py">create</a>(\*\*<a href="src/codex/types/project_create_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="get /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="put /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/codex/types/project_update_params.py">params</a>) -> <a href="./src/codex/types/project_return_schema.py">ProjectReturnSchema</a></code>
- <code title="get /api/projects/">client.projects.<a href="./src/codex/resources/projects/projects.py">list</a>(\*\*<a href="src/codex/types/project_list_params.py">params</a>) -> <a href="./src/codex/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /api/projects/{project_id}">client.projects.<a href="./src/codex/resources/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="get /api/projects/{project_id}/export">client.projects.<a href="./src/codex/resources/projects/projects.py">export</a>(project_id) -> <a href="./src/codex/types/project_export_response.py">object</a></code>

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
from codex.types.projects import Entry, EntryListResponse
```

Methods:

- <code title="post /api/projects/{project_id}/entries/">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">create</a>(project_id, \*\*<a href="src/codex/types/projects/entry_create_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="get /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">retrieve</a>(entry_id, \*, project_id) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="put /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">update</a>(entry_id, \*, project_id, \*\*<a href="src/codex/types/projects/entry_update_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="get /api/projects/{project_id}/entries/">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">list</a>(project_id, \*\*<a href="src/codex/types/projects/entry_list_params.py">params</a>) -> <a href="./src/codex/types/projects/entry_list_response.py">EntryListResponse</a></code>
- <code title="delete /api/projects/{project_id}/entries/{entry_id}">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">delete</a>(entry_id, \*, project_id) -> None</code>
- <code title="post /api/projects/{project_id}/entries/add_question">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">add_question</a>(project_id, \*\*<a href="src/codex/types/projects/entry_add_question_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Entry</a></code>
- <code title="post /api/projects/{project_id}/entries/query">client.projects.entries.<a href="./src/codex/resources/projects/entries.py">query</a>(project_id, \*\*<a href="src/codex/types/projects/entry_query_params.py">params</a>) -> <a href="./src/codex/types/projects/entry.py">Optional[Entry]</a></code>
