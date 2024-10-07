# coding: utf-8

# flake8: noqa

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from bssh_sdk_2.api.basespace_api import BasespaceApi
# import ApiClient
from bssh_sdk_2.api_client import ApiClient
from bssh_sdk_2.configuration import Configuration
# import models into sdk package
from bssh_sdk_2.models.analysis_settings import AnalysisSettings
from bssh_sdk_2.models.api_agreement_compact import ApiAgreementCompact
from bssh_sdk_2.models.app_session_compact import AppSessionCompact
from bssh_sdk_2.models.app_session_ica_logs_step_list_sort_fields_v2_paging import AppSessionIcaLogsStepListSortFieldsV2Paging
from bssh_sdk_2.models.application_metadata import ApplicationMetadata
from bssh_sdk_2.models.application_metadata_v2_api_response import ApplicationMetadataV2ApiResponse
from bssh_sdk_2.models.application_screenshots import ApplicationScreenshots
from bssh_sdk_2.models.application_screenshots_v2_api_response import ApplicationScreenshotsV2ApiResponse
from bssh_sdk_2.models.compute_statistics import ComputeStatistics
from bssh_sdk_2.models.date_time_offset import DateTimeOffset
from bssh_sdk_2.models.genome_compact import GenomeCompact
from bssh_sdk_2.models.i_app_session_compact import IAppSessionCompact
from bssh_sdk_2.models.i_application_compact import IApplicationCompact
from bssh_sdk_2.models.i_biological_sample_compact import IBiologicalSampleCompact
from bssh_sdk_2.models.i_biological_sample_compact_list import IBiologicalSampleCompactList
from bssh_sdk_2.models.i_collection import ICollection
from bssh_sdk_2.models.i_dataset_compact import IDatasetCompact
from bssh_sdk_2.models.i_dictionary import IDictionary
from bssh_sdk_2.models.i_project_compact import IProjectCompact
from bssh_sdk_2.models.i_property_container import IPropertyContainer
from bssh_sdk_2.models.i_user_compact import IUserCompact
from bssh_sdk_2.models.id_files_body import IdFilesBody
from bssh_sdk_2.models.id_files_body1 import IdFilesBody1
from bssh_sdk_2.models.j_container import JContainer
from bssh_sdk_2.models.j_object import JObject
from bssh_sdk_2.models.j_token import JToken
from bssh_sdk_2.models.j_token_equality_comparer import JTokenEqualityComparer
from bssh_sdk_2.models.lane import Lane
from bssh_sdk_2.models.lane_by_read import LaneByRead
from bssh_sdk_2.models.library_container_compact import LibraryContainerCompact
from bssh_sdk_2.models.library_index_compact import LibraryIndexCompact
from bssh_sdk_2.models.library_prep_kit_compact import LibraryPrepKitCompact
from bssh_sdk_2.models.logged_in_user import LoggedInUser
from bssh_sdk_2.models.map_content import MapContent
from bssh_sdk_2.models.metadatuple import Metadatuple
from bssh_sdk_2.models.name_and_id import NameAndId
from bssh_sdk_2.models.o_auth_v2_access_token_request import OAuthV2AccessTokenRequest
from bssh_sdk_2.models.o_auth_v2_access_token_response import OAuthV2AccessTokenResponse
from bssh_sdk_2.models.permissions import Permissions
from bssh_sdk_2.models.prep_module import PrepModule
from bssh_sdk_2.models.prep_module_parameter import PrepModuleParameter
from bssh_sdk_2.models.prep_settings import PrepSettings
from bssh_sdk_2.models.read import Read
from bssh_sdk_2.models.reference import Reference
from bssh_sdk_2.models.registered_instrument_compact import RegisteredInstrumentCompact
from bssh_sdk_2.models.sample_compact import SampleCompact
from bssh_sdk_2.models.sample_library import SampleLibrary
from bssh_sdk_2.models.sequencing_stats_compact import SequencingStatsCompact
from bssh_sdk_2.models.sequencing_stats_per_sample import SequencingStatsPerSample
from bssh_sdk_2.models.species import Species
from bssh_sdk_2.models.storage_statistics import StorageStatistics
from bssh_sdk_2.models.stratus_error_response import StratusErrorResponse
from bssh_sdk_2.models.string_i_collection import StringICollection
from bssh_sdk_2.models.string_i_equality_comparer import StringIEqualityComparer
from bssh_sdk_2.models.string_string_key_value_pair import StringStringKeyValuePair
from bssh_sdk_2.models.string_v2_dataset_attribute_definition_key_collection import StringV2DatasetAttributeDefinitionKeyCollection
from bssh_sdk_2.models.string_v2_dataset_attribute_definition_value_collection import StringV2DatasetAttributeDefinitionValueCollection
from bssh_sdk_2.models.subscription_storage import SubscriptionStorage
from bssh_sdk_2.models.time_span import TimeSpan
from bssh_sdk_2.models.user_notification_event_sort_fields_v2_paging import UserNotificationEventSortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_app_result_compact import V1pre3AppResultCompact
from bssh_sdk_2.models.v1pre3_application import V1pre3Application
from bssh_sdk_2.models.v1pre3_application_compact import V1pre3ApplicationCompact
from bssh_sdk_2.models.v1pre3_application_compact_list import V1pre3ApplicationCompactList
from bssh_sdk_2.models.v1pre3_application_compact_v1pre3_applications_sort_fields_resource_list import V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList
from bssh_sdk_2.models.v1pre3_application_compact_v1pre3_applications_sort_fields_v2_list_response import V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsV2ListResponse
from bssh_sdk_2.models.v1pre3_applications_sort_fields_v2_paging import V1pre3ApplicationsSortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_biological_sample_compact import V1pre3BiologicalSampleCompact
from bssh_sdk_2.models.v1pre3_direct_upload_file import V1pre3DirectUploadFile
from bssh_sdk_2.models.v1pre3_direct_upload_information import V1pre3DirectUploadInformation
from bssh_sdk_2.models.v1pre3_directory_compact import V1pre3DirectoryCompact
from bssh_sdk_2.models.v1pre3_file import V1pre3File
from bssh_sdk_2.models.v1pre3_file_compact import V1pre3FileCompact
from bssh_sdk_2.models.v1pre3_file_compact_list import V1pre3FileCompactList
from bssh_sdk_2.models.v1pre3_files_sort_fields_v2_paging import V1pre3FilesSortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_library_pool_compact import V1pre3LibraryPoolCompact
from bssh_sdk_2.models.v1pre3_post_dataset_id_direct_upload_info_request import V1pre3PostDatasetIdDirectUploadInfoRequest
from bssh_sdk_2.models.v1pre3_post_resource_id_files_request import V1pre3PostResourceIdFilesRequest
from bssh_sdk_2.models.v1pre3_post_trash_item_restore_from_trash_request import V1pre3PostTrashItemRestoreFromTrashRequest
from bssh_sdk_2.models.v1pre3_project import V1pre3Project
from bssh_sdk_2.models.v1pre3_project_compact import V1pre3ProjectCompact
from bssh_sdk_2.models.v1pre3_property_item_sort_fields_v2_paging import V1pre3PropertyItemSortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_property_options_request import V1pre3PropertyOptionsRequest
from bssh_sdk_2.models.v1pre3_property_sort_fields_v2_paging import V1pre3PropertySortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_run_compact import V1pre3RunCompact
from bssh_sdk_2.models.v1pre3_trash_item import V1pre3TrashItem
from bssh_sdk_2.models.v1pre3_trash_item_compact import V1pre3TrashItemCompact
from bssh_sdk_2.models.v1pre3_trash_item_compact_list import V1pre3TrashItemCompactList
from bssh_sdk_2.models.v1pre3_trash_items_sort_fields_v2_paging import V1pre3TrashItemsSortFieldsV2Paging
from bssh_sdk_2.models.v1pre3_user_compact import V1pre3UserCompact
from bssh_sdk_2.models.v2_aggregate_usage import V2AggregateUsage
from bssh_sdk_2.models.v2_agreement import V2Agreement
from bssh_sdk_2.models.v2_agreement_compact import V2AgreementCompact
from bssh_sdk_2.models.v2_analysis_workflow_dependencies_response import V2AnalysisWorkflowDependenciesResponse
from bssh_sdk_2.models.v2_analysis_workflow_dependency import V2AnalysisWorkflowDependency
from bssh_sdk_2.models.v2_app_session import V2AppSession
from bssh_sdk_2.models.v2_app_session_compact import V2AppSessionCompact
from bssh_sdk_2.models.v2_app_session_compact_list import V2AppSessionCompactList
from bssh_sdk_2.models.v2_app_session_ica_log_path import V2AppSessionIcaLogPath
from bssh_sdk_2.models.v2_app_session_ica_log_path_list import V2AppSessionIcaLogPathList
from bssh_sdk_2.models.v2_app_session_ica_step_log import V2AppSessionIcaStepLog
from bssh_sdk_2.models.v2_app_session_ica_step_log_compact import V2AppSessionIcaStepLogCompact
from bssh_sdk_2.models.v2_app_session_ica_step_log_compact_list import V2AppSessionIcaStepLogCompactList
from bssh_sdk_2.models.v2_app_sessions_sort_fields_v2_paging import V2AppSessionsSortFieldsV2Paging
from bssh_sdk_2.models.v2_application_settings import V2ApplicationSettings
from bssh_sdk_2.models.v2_biological_sample import V2BiologicalSample
from bssh_sdk_2.models.v2_biological_sample_compact import V2BiologicalSampleCompact
from bssh_sdk_2.models.v2_biological_sample_compact_list import V2BiologicalSampleCompactList
from bssh_sdk_2.models.v2_biological_sample_library_yield import V2BiologicalSampleLibraryYield
from bssh_sdk_2.models.v2_biological_samples_sort_fields_v2_paging import V2BiologicalSamplesSortFieldsV2Paging
from bssh_sdk_2.models.v2_bulk_archive_request import V2BulkArchiveRequest
from bssh_sdk_2.models.v2_bulk_data_compress_request import V2BulkDataCompressRequest
from bssh_sdk_2.models.v2_bulk_restore_request import V2BulkRestoreRequest
from bssh_sdk_2.models.v2_bulk_unzip_request import V2BulkUnzipRequest
from bssh_sdk_2.models.v2_comment import V2Comment
from bssh_sdk_2.models.v2_comment_list import V2CommentList
from bssh_sdk_2.models.v2_comment_sort_fields_v2_paging import V2CommentSortFieldsV2Paging
from bssh_sdk_2.models.v2_create_biological_sample_request import V2CreateBiologicalSampleRequest
from bssh_sdk_2.models.v2_create_existing_library_lab_requeue_request import V2CreateExistingLibraryLabRequeueRequest
from bssh_sdk_2.models.v2_create_existing_pool_lab_requeue_request import V2CreateExistingPoolLabRequeueRequest
from bssh_sdk_2.models.v2_create_instrument_diagnostic_request import V2CreateInstrumentDiagnosticRequest
from bssh_sdk_2.models.v2_create_instrument_jwt_request import V2CreateInstrumentJwtRequest
from bssh_sdk_2.models.v2_create_new_library_lab_requeue_request import V2CreateNewLibraryLabRequeueRequest
from bssh_sdk_2.models.v2_dataset import V2Dataset
from bssh_sdk_2.models.v2_dataset_attribute_definition import V2DatasetAttributeDefinition
from bssh_sdk_2.models.v2_dataset_compact import V2DatasetCompact
from bssh_sdk_2.models.v2_dataset_compact_list import V2DatasetCompactList
from bssh_sdk_2.models.v2_dataset_type import V2DatasetType
from bssh_sdk_2.models.v2_dataset_type_attribute_schema import V2DatasetTypeAttributeSchema
from bssh_sdk_2.models.v2_dataset_type_compact import V2DatasetTypeCompact
from bssh_sdk_2.models.v2_datasets_sort_fields_v2_paging import V2DatasetsSortFieldsV2Paging
from bssh_sdk_2.models.v2_error import V2Error
from bssh_sdk_2.models.v2_files_list import V2FilesList
from bssh_sdk_2.models.v2_gds_file_upload_request import V2GdsFileUploadRequest
from bssh_sdk_2.models.v2_ica_complete_upload_request import V2IcaCompleteUploadRequest
from bssh_sdk_2.models.v2_ica_file_create_download_url_request import V2IcaFileCreateDownloadUrlRequest
from bssh_sdk_2.models.v2_ica_file_upload_request import V2IcaFileUploadRequest
from bssh_sdk_2.models.v2_instrument_compact import V2InstrumentCompact
from bssh_sdk_2.models.v2_instrument_compact_list import V2InstrumentCompactList
from bssh_sdk_2.models.v2_instrument_diagnostic import V2InstrumentDiagnostic
from bssh_sdk_2.models.v2_instrument_error_response import V2InstrumentErrorResponse
from bssh_sdk_2.models.v2_instrument_jwt import V2InstrumentJwt
from bssh_sdk_2.models.v2_instrument_sort_fields_v2_paging import V2InstrumentSortFieldsV2Paging
from bssh_sdk_2.models.v2_instrument_stat import V2InstrumentStat
from bssh_sdk_2.models.v2_instrument_stat_list import V2InstrumentStatList
from bssh_sdk_2.models.v2_instrument_statistics_sort_fields_v2_paging import V2InstrumentStatisticsSortFieldsV2Paging
from bssh_sdk_2.models.v2_instrument_stats_bin import V2InstrumentStatsBin
from bssh_sdk_2.models.v2_instrument_status_compact import V2InstrumentStatusCompact
from bssh_sdk_2.models.v2_instrument_status_compact_list import V2InstrumentStatusCompactList
from bssh_sdk_2.models.v2_lab_requeue import V2LabRequeue
from bssh_sdk_2.models.v2_lab_requeue_compact import V2LabRequeueCompact
from bssh_sdk_2.models.v2_lab_requeue_compact_list import V2LabRequeueCompactList
from bssh_sdk_2.models.v2_lab_requeue_list import V2LabRequeueList
from bssh_sdk_2.models.v2_lab_requeue_sort_fields_v2_paging import V2LabRequeueSortFieldsV2Paging
from bssh_sdk_2.models.v2_library_compact import V2LibraryCompact
from bssh_sdk_2.models.v2_library_compact_extended import V2LibraryCompactExtended
from bssh_sdk_2.models.v2_library_compact_extended_v2_library_sort_fields_resource_list import V2LibraryCompactExtendedV2LibrarySortFieldsResourceList
from bssh_sdk_2.models.v2_library_compact_list import V2LibraryCompactList
from bssh_sdk_2.models.v2_library_sort_fields_v2_paging import V2LibrarySortFieldsV2Paging
from bssh_sdk_2.models.v2_migration_status_report import V2MigrationStatusReport
from bssh_sdk_2.models.v2_notification_info import V2NotificationInfo
from bssh_sdk_2.models.v2_o_auth_v1_from_o_auth_v2_request import V2OAuthV1FromOAuthV2Request
from bssh_sdk_2.models.v2_o_auth_v1_token import V2OAuthV1Token
from bssh_sdk_2.models.v2_o_auth_v2_token import V2OAuthV2Token
from bssh_sdk_2.models.v2_o_auth_v2_token_from_application_jwt_request import V2OAuthV2TokenFromApplicationJwtRequest
from bssh_sdk_2.models.v2_o_auth_v2_token_request import V2OAuthV2TokenRequest
from bssh_sdk_2.models.v2_part_etag import V2PartEtag
from bssh_sdk_2.models.v2_part_info import V2PartInfo
from bssh_sdk_2.models.v2_period_aggregate_usage import V2PeriodAggregateUsage
from bssh_sdk_2.models.v2_period_aggregate_usage_list import V2PeriodAggregateUsageList
from bssh_sdk_2.models.v2_period_aggregate_usage_sort_fields_v2_paging import V2PeriodAggregateUsageSortFieldsV2Paging
from bssh_sdk_2.models.v2_post_app_sessions_id_files_request import V2PostAppSessionsIdFilesRequest
from bssh_sdk_2.models.v2_post_app_sessions_id_request import V2PostAppSessionsIdRequest
from bssh_sdk_2.models.v2_post_app_sessions_id_reschedule_request import V2PostAppSessionsIdRescheduleRequest
from bssh_sdk_2.models.v2_post_app_sessions_id_stop_request import V2PostAppSessionsIdStopRequest
from bssh_sdk_2.models.v2_post_app_sessions_properties_request import V2PostAppSessionsPropertiesRequest
from bssh_sdk_2.models.v2_post_app_sessions_track_request import V2PostAppSessionsTrackRequest
from bssh_sdk_2.models.v2_post_app_sessions_workflow_sessions_track_request import V2PostAppSessionsWorkflowSessionsTrackRequest
from bssh_sdk_2.models.v2_post_application_id_workflows_request import V2PostApplicationIdWorkflowsRequest
from bssh_sdk_2.models.v2_post_appsessions_request import V2PostAppsessionsRequest
from bssh_sdk_2.models.v2_post_bio_samples_bulk_update_request import V2PostBioSamplesBulkUpdateRequest
from bssh_sdk_2.models.v2_post_bio_samples_id_aggregation_request import V2PostBioSamplesIdAggregationRequest
from bssh_sdk_2.models.v2_post_biosample_library_request import V2PostBiosampleLibraryRequest
from bssh_sdk_2.models.v2_post_datasets_id_copy_request import V2PostDatasetsIdCopyRequest
from bssh_sdk_2.models.v2_post_datasets_id_request import V2PostDatasetsIdRequest
from bssh_sdk_2.models.v2_post_datasets_request import V2PostDatasetsRequest
from bssh_sdk_2.models.v2_post_instrument_errors_request import V2PostInstrumentErrorsRequest
from bssh_sdk_2.models.v2_post_lanes_id_request import V2PostLanesIdRequest
from bssh_sdk_2.models.v2_post_library_pool_id_request import V2PostLibraryPoolIdRequest
from bssh_sdk_2.models.v2_post_projects_id_datasets_request import V2PostProjectsIdDatasetsRequest
from bssh_sdk_2.models.v2_post_projects_request import V2PostProjectsRequest
from bssh_sdk_2.models.v2_post_publish_app_session_status_request import V2PostPublishAppSessionStatusRequest
from bssh_sdk_2.models.v2_post_run_id_request import V2PostRunIdRequest
from bssh_sdk_2.models.v2_post_runs_request import V2PostRunsRequest
from bssh_sdk_2.models.v2_post_runs_start_request import V2PostRunsStartRequest
from bssh_sdk_2.models.v2_post_signed_url_validation_request import V2PostSignedUrlValidationRequest
from bssh_sdk_2.models.v2_post_user_settings_request import V2PostUserSettingsRequest
from bssh_sdk_2.models.v2_post_users_current_request import V2PostUsersCurrentRequest
from bssh_sdk_2.models.v2_post_users_id_analysis_config_template_request import V2PostUsersIdAnalysisConfigTemplateRequest
from bssh_sdk_2.models.v2_post_users_id_v2_bio_sample_registry_request import V2PostUsersIdV2BioSampleRegistryRequest
from bssh_sdk_2.models.v2_prep_request import V2PrepRequest
from bssh_sdk_2.models.v2_presigned_url_for_upload import V2PresignedUrlForUpload
from bssh_sdk_2.models.v2_product_usage import V2ProductUsage
from bssh_sdk_2.models.v2_property import V2Property
from bssh_sdk_2.models.v2_property_compact import V2PropertyCompact
from bssh_sdk_2.models.v2_property_compact_list import V2PropertyCompactList
from bssh_sdk_2.models.v2_property_container import V2PropertyContainer
from bssh_sdk_2.models.v2_property_for_posts import V2PropertyForPosts
from bssh_sdk_2.models.v2_property_item import V2PropertyItem
from bssh_sdk_2.models.v2_property_item_list import V2PropertyItemList
from bssh_sdk_2.models.v2_qc_threshold import V2QcThreshold
from bssh_sdk_2.models.v2_qc_threshold_response import V2QcThresholdResponse
from bssh_sdk_2.models.v2_resource_manifest import V2ResourceManifest
from bssh_sdk_2.models.v2_resource_manifest_compact import V2ResourceManifestCompact
from bssh_sdk_2.models.v2_resource_manifest_sort_fields_v2_paging import V2ResourceManifestSortFieldsV2Paging
from bssh_sdk_2.models.v2_resource_presigned_url_complete_request import V2ResourcePresignedUrlCompleteRequest
from bssh_sdk_2.models.v2_resource_presigned_url_complete_request_for_everyone import V2ResourcePresignedUrlCompleteRequestForEveryone
from bssh_sdk_2.models.v2_run import V2Run
from bssh_sdk_2.models.v2_run_access import V2RunAccess
from bssh_sdk_2.models.v2_run_compact import V2RunCompact
from bssh_sdk_2.models.v2_run_compact_list import V2RunCompactList
from bssh_sdk_2.models.v2_run_compact_summary import V2RunCompactSummary
from bssh_sdk_2.models.v2_run_instrument_compact import V2RunInstrumentCompact
from bssh_sdk_2.models.v2_run_lane_summary import V2RunLaneSummary
from bssh_sdk_2.models.v2_run_lane_summary_list import V2RunLaneSummaryList
from bssh_sdk_2.models.v2_run_lane_summary_sort_fields_v2_paging import V2RunLaneSummarySortFieldsV2Paging
from bssh_sdk_2.models.v2_run_sample_sheet import V2RunSampleSheet
from bssh_sdk_2.models.v2_run_sample_sheet_application import V2RunSampleSheetApplication
from bssh_sdk_2.models.v2_runs_sort_fields_v2_paging import V2RunsSortFieldsV2Paging
from bssh_sdk_2.models.v2_sequencing_stats import V2SequencingStats
from bssh_sdk_2.models.v2_sign_agreement_request import V2SignAgreementRequest
from bssh_sdk_2.models.v2_signed_url_validation import V2SignedUrlValidation
from bssh_sdk_2.models.v2_software import V2Software
from bssh_sdk_2.models.v2_subject_compact import V2SubjectCompact
from bssh_sdk_2.models.v2_update_biological_sample_request import V2UpdateBiologicalSampleRequest
from bssh_sdk_2.models.v2_update_instrument_diagnostic_request import V2UpdateInstrumentDiagnosticRequest
from bssh_sdk_2.models.v2_user import V2User
from bssh_sdk_2.models.v2_user_account_transfer_request import V2UserAccountTransferRequest
from bssh_sdk_2.models.v2_user_agreement_compact import V2UserAgreementCompact
from bssh_sdk_2.models.v2_user_agreement_compact_list import V2UserAgreementCompactList
from bssh_sdk_2.models.v2_user_agreements_sort_fields_v2_paging import V2UserAgreementsSortFieldsV2Paging
from bssh_sdk_2.models.v2_user_compact import V2UserCompact
from bssh_sdk_2.models.v2_user_notification_compact import V2UserNotificationCompact
from bssh_sdk_2.models.v2_user_notification_compact_list import V2UserNotificationCompactList
from bssh_sdk_2.models.v2_user_setting import V2UserSetting
from bssh_sdk_2.models.v2_user_setting_list import V2UserSettingList
from bssh_sdk_2.models.v2_user_settings_response import V2UserSettingsResponse
from bssh_sdk_2.models.v2_user_settings_sort_fields_v2_paging import V2UserSettingsSortFieldsV2Paging
from bssh_sdk_2.models.v2_user_subscription import V2UserSubscription
from bssh_sdk_2.models.v2_workgroup import V2Workgroup
from bssh_sdk_2.models.v2_workgroup_list import V2WorkgroupList
from bssh_sdk_2.models.v2_workgroup_sort_fields_v2_paging import V2WorkgroupSortFieldsV2Paging
from bssh_sdk_2.models.wallet import Wallet