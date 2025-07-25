# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T01:11:58+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Query

from models import (
    AbandonReleaseRequest,
    AbandonReleaseResponse,
    AdvanceRolloutRequest,
    AdvanceRolloutResponse,
    Alt,
    ApproveRolloutRequest,
    ApproveRolloutResponse,
    CancelOperationRequest,
    DeliveryPipeline,
    Empty,
    FieldXgafv,
    IgnoreJobRequest,
    IgnoreJobResponse,
    ListDeliveryPipelinesResponse,
    ListJobRunsResponse,
    ListLocationsResponse,
    ListOperationsResponse,
    ListReleasesResponse,
    ListRolloutsResponse,
    ListTargetsResponse,
    Operation,
    Policy,
    Release,
    RetryJobRequest,
    RetryJobResponse,
    Rollout,
    SetIamPolicyRequest,
    Target,
    TerminateJobRunRequest,
    TerminateJobRunResponse,
    TestIamPermissionsRequest,
    TestIamPermissionsResponse,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Google Cloud Deploy API',
    version='v1',
    servers=[{'url': 'https://clouddeploy.googleapis.com/'}],
)


@app.delete(
    '/v1/{name}',
    description=""" Deletes a single Target. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
        'workflow_operation_management',
        'iam_policy_operations',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_delete(
    name: str,
    allow_missing: Optional[bool] = Query(None, alias='allowMissing'),
    etag: Optional[str] = None,
    request_id: Optional[str] = Query(None, alias='requestId'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}',
    description=""" Gets details of a single Target. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
        'workflow_operation_management',
        'iam_policy_operations',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_get(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/{name}',
    description=""" Updates the parameters of a single Target. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_patch(
    name: str,
    allow_missing: Optional[bool] = Query(None, alias='allowMissing'),
    request_id: Optional[str] = Query(None, alias='requestId'),
    update_mask: Optional[str] = Query(None, alias='updateMask'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Target = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}/locations',
    description=""" Lists information about the supported locations for this service. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
        'workflow_operation_management',
        'iam_policy_operations',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}/operations',
    description=""" Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. """,
    tags=['pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_operations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:abandon',
    description=""" Abandons a Release in the Delivery Pipeline. """,
    tags=['pipeline_operations_management', 'deployment_rollout_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def abandon_delivery_pipeline_release(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: AbandonReleaseRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:advance',
    description=""" Advances a Rollout in a given project and location. """,
    tags=['pipeline_operations_management', 'deployment_rollout_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def advance_rollout_deployment_process(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: AdvanceRolloutRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:approve',
    description=""" Approves a Rollout. """,
    tags=['deployment_rollout_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def approve_delivery_pipeline_rollout(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: ApproveRolloutRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:cancel',
    description=""" Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. """,
    tags=['workflow_operation_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_operations_cancel(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: CancelOperationRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:terminate',
    description=""" Terminates a Job Run in a given project and location. """,
    tags=['job_execution_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def terminate_job_run(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: TerminateJobRunRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/deliveryPipelines',
    description=""" Lists DeliveryPipelines in a given project and location. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
        'workflow_operation_management',
        'iam_policy_operations',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_delivery_pipelines_list(
    parent: str,
    filter: Optional[str] = None,
    order_by: Optional[str] = Query(None, alias='orderBy'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/deliveryPipelines',
    description=""" Creates a new DeliveryPipeline in a given project and location. """,
    tags=['pipeline_operations_management', 'deployment_rollout_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_delivery_pipelines_create(
    parent: str,
    delivery_pipeline_id: Optional[str] = Query(None, alias='deliveryPipelineId'),
    request_id: Optional[str] = Query(None, alias='requestId'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: DeliveryPipeline = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/jobRuns',
    description=""" Lists JobRuns in a given project and location. """,
    tags=['target_configuration_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def list_job_runs_for_delivery_pipeline(
    parent: str,
    filter: Optional[str] = None,
    order_by: Optional[str] = Query(None, alias='orderBy'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/releases',
    description=""" Lists Releases in a given project and location. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'workflow_operation_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_delivery_pipelines_releases_list(
    parent: str,
    filter: Optional[str] = None,
    order_by: Optional[str] = Query(None, alias='orderBy'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/releases',
    description=""" Creates a new Release in a given project and location. """,
    tags=['pipeline_operations_management', 'deployment_rollout_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def create_release_in_delivery_pipeline(
    parent: str,
    release_id: Optional[str] = Query(None, alias='releaseId'),
    request_id: Optional[str] = Query(None, alias='requestId'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Release = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/rollouts',
    description=""" Lists Rollouts in a given project and location. """,
    tags=[
        'target_configuration_management',
        'pipeline_operations_management',
        'deployment_rollout_management',
        'workflow_operation_management',
        'iam_policy_operations',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def list_delivery_pipeline_releases_rollouts(
    parent: str,
    filter: Optional[str] = None,
    order_by: Optional[str] = Query(None, alias='orderBy'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/rollouts',
    description=""" Creates a new Rollout in a given project and location. """,
    tags=['deployment_rollout_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def create_rollout_for_delivery_pipeline(
    parent: str,
    request_id: Optional[str] = Query(None, alias='requestId'),
    rollout_id: Optional[str] = Query(None, alias='rolloutId'),
    starting_phase_id: Optional[str] = Query(None, alias='startingPhaseId'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Rollout = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/targets',
    description=""" Lists Targets in a given project and location. """,
    tags=['target_configuration_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_list(
    parent: str,
    filter: Optional[str] = None,
    order_by: Optional[str] = Query(None, alias='orderBy'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/targets',
    description=""" Creates a new Target in a given project and location. """,
    tags=[
        'target_configuration_management',
        'deployment_rollout_management',
        'workflow_operation_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_create(
    parent: str,
    request_id: Optional[str] = Query(None, alias='requestId'),
    target_id: Optional[str] = Query(None, alias='targetId'),
    validate_only: Optional[bool] = Query(None, alias='validateOnly'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Target = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{resource}:getIamPolicy',
    description=""" Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. """,
    tags=['iam_policy_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_get_iam_policy(
    resource: str,
    options_requested_policy_version: Optional[int] = Query(
        None, alias='options.requestedPolicyVersion'
    ),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{resource}:setIamPolicy',
    description=""" Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. """,
    tags=['iam_policy_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_set_iam_policy(
    resource: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: SetIamPolicyRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{resource}:testIamPermissions',
    description=""" Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. """,
    tags=['iam_policy_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def clouddeploy_projects_locations_targets_test_iam_permissions(
    resource: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: TestIamPermissionsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{rollout}:ignoreJob',
    description=""" Ignores the specified Job in a Rollout. """,
    tags=[
        'pipeline_operations_management',
        'deployment_rollout_management',
        'job_execution_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def ignore_job_for_rollout(
    rollout: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: IgnoreJobRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{rollout}:retryJob',
    description=""" Retries the specified Job in a Rollout. """,
    tags=['deployment_rollout_management', 'pipeline_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def retry_job_for_rollout(
    rollout: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: RetryJobRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
