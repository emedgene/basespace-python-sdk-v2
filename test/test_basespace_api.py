# coding: utf-8

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.basespace_api import BasespaceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBasespaceApi(unittest.TestCase):
    """BasespaceApi unit test stubs"""

    def setUp(self):
        self.api = BasespaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_v2_appsessions_id(self):
        """Test case for delete_v2_appsessions_id

        Delete a specific analysis  # noqa: E501
        """
        pass

    def test_delete_v2_appsessions_id_properties_name(self):
        """Test case for delete_v2_appsessions_id_properties_name

        Delete a property of an analysis  # noqa: E501
        """
        pass

    def test_delete_v2_icauploads_foldertype_dataid(self):
        """Test case for delete_v2_icauploads_foldertype_dataid

        """
        pass

    def test_delete_v2_notifications_id(self):
        """Test case for delete_v2_notifications_id

        """
        pass

    def test_delete_v2_oauthv2tokens_current(self):
        """Test case for delete_v2_oauthv2tokens_current

        """
        pass

    def test_delete_v2_session_invalidate(self):
        """Test case for delete_v2_session_invalidate

        Log out user from Sequence Hub and end session  # noqa: E501
        """
        pass

    def test_delete_v2_trash(self):
        """Test case for delete_v2_trash

        Delete all items in the trash  # noqa: E501
        """
        pass

    def test_get_v2_agreements_id(self):
        """Test case for get_v2_agreements_id

        Get detailed information about a single agreement  # noqa: E501
        """
        pass

    def test_get_v2_applicationmetadata(self):
        """Test case for get_v2_applicationmetadata

        Request metadata about applications  # noqa: E501
        """
        pass

    def test_get_v2_applications(self):
        """Test case for get_v2_applications

        Get a list of available applications  # noqa: E501
        """
        pass

    def test_get_v2_applications_id(self):
        """Test case for get_v2_applications_id

        Get information about an app  # noqa: E501
        """
        pass

    def test_get_v2_applications_id_qcthresholds(self):
        """Test case for get_v2_applications_id_qcthresholds

        Get a list of QC thresholds applied to an analysis workflow  # noqa: E501
        """
        pass

    def test_get_v2_applications_id_screenshots(self):
        """Test case for get_v2_applications_id_screenshots

        Get screenshots of an app  # noqa: E501
        """
        pass

    def test_get_v2_applications_id_settings(self):
        """Test case for get_v2_applications_id_settings

        Get the settings of an application or workflow  # noqa: E501
        """
        pass

    def test_get_v2_applications_id_versions(self):
        """Test case for get_v2_applications_id_versions

        Get versions of an app  # noqa: E501
        """
        pass

    def test_get_v2_applications_id_workflowdependencies(self):
        """Test case for get_v2_applications_id_workflowdependencies

        Get a list of workflow dependencies on an analysis workflow  # noqa: E501
        """
        pass

    def test_get_v2_appresults_id_file_upload_info(self):
        """Test case for get_v2_appresults_id_file_upload_info

        """
        pass

    def test_get_v2_appsessions(self):
        """Test case for get_v2_appsessions

        Get a list of analyses  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id(self):
        """Test case for get_v2_appsessions_id

        Get information about an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_comments(self):
        """Test case for get_v2_appsessions_id_comments

        Get a list of comments made about an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs(self):
        """Test case for get_v2_appsessions_id_icalogs

        Get ICA log steps for workflows and analyses  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_analyses_analysisid_stepid(self):
        """Test case for get_v2_appsessions_id_icalogs_analyses_analysisid_stepid

        Get ICA analysis log step stdout stderr log paths  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr(self):
        """Test case for get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr

        Get ICA analysis step stderr log  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout(self):
        """Test case for get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout

        Get ICA analysis step stdout log  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_analyses_icaanalysisid(self):
        """Test case for get_v2_appsessions_id_icalogs_analyses_icaanalysisid

        Get ICA analysis log steps  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_orchestrated_analyses(self):
        """Test case for get_v2_appsessions_id_icalogs_orchestrated_analyses

        Get orchestrated analyses  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_workflowsession(self):
        """Test case for get_v2_appsessions_id_icalogs_workflowsession

        Get ICA workflow session log steps  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_workflowsession_stepid(self):
        """Test case for get_v2_appsessions_id_icalogs_workflowsession_stepid

        Get ICA workflow session log step stdout stderr log paths  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr(self):
        """Test case for get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr

        Get ICA workflow session log step stderr  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout(self):
        """Test case for get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout

        Get ICA workflow session log step stdout  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_logfiles(self):
        """Test case for get_v2_appsessions_id_logfiles

        Get a list of logs of an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_properties(self):
        """Test case for get_v2_appsessions_id_properties

        Get a list of properties of an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_properties_name(self):
        """Test case for get_v2_appsessions_id_properties_name

        Get information about a property of an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_properties_name_items(self):
        """Test case for get_v2_appsessions_id_properties_name_items

        Get a list of items from a property of an analysis  # noqa: E501
        """
        pass

    def test_get_v2_appsessions_id_reports(self):
        """Test case for get_v2_appsessions_id_reports

        """
        pass

    def test_get_v2_archivingstats(self):
        """Test case for get_v2_archivingstats

        Get a summary of total archiving Data Managment Events , their status  .  # noqa: E501
        """
        pass

    def test_get_v2_archivingstatsdetails(self):
        """Test case for get_v2_archivingstatsdetails

        Get list of archiving Data Managment Events , their status  .  # noqa: E501
        """
        pass

    def test_get_v2_autodeletionevents(self):
        """Test case for get_v2_autodeletionevents

        Get a list of all auto-deletion events.  # noqa: E501
        """
        pass

    def test_get_v2_autodeletionpipeline(self):
        """Test case for get_v2_autodeletionpipeline

        Get the list of users who have entered the auto-deletion pipeline due to inactivity or exceeding their storage limit.  # noqa: E501
        """
        pass

    def test_get_v2_autodeletionusers(self):
        """Test case for get_v2_autodeletionusers

        Get a summary of users who are about to have their account data deleted due to data retention policy.  # noqa: E501
        """
        pass

    def test_get_v2_biosamples(self):
        """Test case for get_v2_biosamples

        Get a list of biosamples  # noqa: E501
        """
        pass

    def test_get_v2_biosamples_biosampleid_labrequeues(self):
        """Test case for get_v2_biosamples_biosampleid_labrequeues

        Get a list of a biosample�s lab requeues  # noqa: E501
        """
        pass

    def test_get_v2_biosamples_id(self):
        """Test case for get_v2_biosamples_id

        Get information about a biosample  # noqa: E501
        """
        pass

    def test_get_v2_biosamples_id_aggregatedfastqdatasets(self):
        """Test case for get_v2_biosamples_id_aggregatedfastqdatasets

        Get aggregated datasets for a given biosample  # noqa: E501
        """
        pass

    def test_get_v2_biosamples_id_libraries(self):
        """Test case for get_v2_biosamples_id_libraries

        Get a list of a biosample�s libraries  # noqa: E501
        """
        pass

    def test_get_v2_biosamples_id_properties(self):
        """Test case for get_v2_biosamples_id_properties

        """
        pass

    def test_get_v2_biosamples_id_properties_name(self):
        """Test case for get_v2_biosamples_id_properties_name

        """
        pass

    def test_get_v2_biosamples_id_properties_name_items(self):
        """Test case for get_v2_biosamples_id_properties_name_items

        """
        pass

    def test_get_v2_biosamples_id_runlanesummaries(self):
        """Test case for get_v2_biosamples_id_runlanesummaries

        Get information about biosample’s lane mapping  # noqa: E501
        """
        pass

    def test_get_v2_datasets(self):
        """Test case for get_v2_datasets

        Get a list of datasets  # noqa: E501
        """
        pass

    def test_get_v2_datasets_id(self):
        """Test case for get_v2_datasets_id

        Get information about a dataset  # noqa: E501
        """
        pass

    def test_get_v2_datasets_id_comments(self):
        """Test case for get_v2_datasets_id_comments

        Get a list of comments made about a dataset  # noqa: E501
        """
        pass

    def test_get_v2_datasets_id_direct_upload_info(self):
        """Test case for get_v2_datasets_id_direct_upload_info

        """
        pass

    def test_get_v2_datasets_id_file_upload_info(self):
        """Test case for get_v2_datasets_id_file_upload_info

        """
        pass

    def test_get_v2_datasets_id_files(self):
        """Test case for get_v2_datasets_id_files

        Get a list of files of a dataset  # noqa: E501
        """
        pass

    def test_get_v2_datasets_id_properties(self):
        """Test case for get_v2_datasets_id_properties

        """
        pass

    def test_get_v2_datasets_id_properties_name(self):
        """Test case for get_v2_datasets_id_properties_name

        """
        pass

    def test_get_v2_datasets_id_properties_name_items(self):
        """Test case for get_v2_datasets_id_properties_name_items

        """
        pass

    def test_get_v2_datasettypes_id(self):
        """Test case for get_v2_datasettypes_id

        Get information about a dataset type  # noqa: E501
        """
        pass

    def test_get_v2_gdssharetransferstats(self):
        """Test case for get_v2_gdssharetransferstats

        Get a summary of GDS share or transfer operations.  # noqa: E501
        """
        pass

    def test_get_v2_instrumentconnectioncheck_file_upload_info(self):
        """Test case for get_v2_instrumentconnectioncheck_file_upload_info

        """
        pass

    def test_get_v2_instrumentdiagnostics_id(self):
        """Test case for get_v2_instrumentdiagnostics_id

        """
        pass

    def test_get_v2_instruments(self):
        """Test case for get_v2_instruments

        """
        pass

    def test_get_v2_instrumentstatistics(self):
        """Test case for get_v2_instrumentstatistics

        Get instrument statistics  # noqa: E501
        """
        pass

    def test_get_v2_instrumentstatus(self):
        """Test case for get_v2_instrumentstatus

        """
        pass

    def test_get_v2_labrequeues(self):
        """Test case for get_v2_labrequeues

        Get a list of lab requeues  # noqa: E501
        """
        pass

    def test_get_v2_labrequeues_id(self):
        """Test case for get_v2_labrequeues_id

        Get information about a specific labrequeue  # noqa: E501
        """
        pass

    def test_get_v2_laneqcthresholds(self):
        """Test case for get_v2_laneqcthresholds

        Get a list of QC thresholds applied to lanes  # noqa: E501
        """
        pass

    def test_get_v2_lanes_id(self):
        """Test case for get_v2_lanes_id

        Get information about a lane  # noqa: E501
        """
        pass

    def test_get_v2_lanes_id_comments(self):
        """Test case for get_v2_lanes_id_comments

        Get a list of comments on a lane  # noqa: E501
        """
        pass

    def test_get_v2_libraries(self):
        """Test case for get_v2_libraries

        Get a list of libraries  # noqa: E501
        """
        pass

    def test_get_v2_libraries_id_properties(self):
        """Test case for get_v2_libraries_id_properties

        """
        pass

    def test_get_v2_libraries_id_properties_name(self):
        """Test case for get_v2_libraries_id_properties_name

        """
        pass

    def test_get_v2_libraries_id_properties_name_items(self):
        """Test case for get_v2_libraries_id_properties_name_items

        """
        pass

    def test_get_v2_librarypools(self):
        """Test case for get_v2_librarypools

        Get a list of library pools  # noqa: E501
        """
        pass

    def test_get_v2_librarypools_id_libraries(self):
        """Test case for get_v2_librarypools_id_libraries

        Get a list of libraries of a pool  # noqa: E501
        """
        pass

    def test_get_v2_librarypools_id_properties(self):
        """Test case for get_v2_librarypools_id_properties

        """
        pass

    def test_get_v2_librarypools_id_properties_name(self):
        """Test case for get_v2_librarypools_id_properties_name

        """
        pass

    def test_get_v2_librarypools_id_properties_name_items(self):
        """Test case for get_v2_librarypools_id_properties_name_items

        """
        pass

    def test_get_v2_projects_id(self):
        """Test case for get_v2_projects_id

        Get information about a project  # noqa: E501
        """
        pass

    def test_get_v2_projects_id_datasets(self):
        """Test case for get_v2_projects_id_datasets

        Get a list of datasets in a project  # noqa: E501
        """
        pass

    def test_get_v2_projects_id_properties(self):
        """Test case for get_v2_projects_id_properties

        """
        pass

    def test_get_v2_projects_id_properties_name(self):
        """Test case for get_v2_projects_id_properties_name

        """
        pass

    def test_get_v2_projects_id_properties_name_items(self):
        """Test case for get_v2_projects_id_properties_name_items

        """
        pass

    def test_get_v2_resourcemanifest(self):
        """Test case for get_v2_resourcemanifest

        Get a manifest of filesets for the requested resources (max 300 items)  # noqa: E501
        """
        pass

    def test_get_v2_runs(self):
        """Test case for get_v2_runs

        Get a list of runs accessible by current user  # noqa: E501
        """
        pass

    def test_get_v2_runs_accesscheck(self):
        """Test case for get_v2_runs_accesscheck

        """
        pass

    def test_get_v2_runs_id(self):
        """Test case for get_v2_runs_id

        Get information about a run  # noqa: E501
        """
        pass

    def test_get_v2_runs_id_file_upload_info(self):
        """Test case for get_v2_runs_id_file_upload_info

        """
        pass

    def test_get_v2_runs_id_files(self):
        """Test case for get_v2_runs_id_files

        Get a list of files of a run  # noqa: E501
        """
        pass

    def test_get_v2_runs_id_properties(self):
        """Test case for get_v2_runs_id_properties

        """
        pass

    def test_get_v2_runs_id_properties_name(self):
        """Test case for get_v2_runs_id_properties_name

        """
        pass

    def test_get_v2_runs_id_properties_name_items(self):
        """Test case for get_v2_runs_id_properties_name_items

        """
        pass

    def test_get_v2_runs_id_samplesheet(self):
        """Test case for get_v2_runs_id_samplesheet

        """
        pass

    def test_get_v2_runs_id_sequencingstats(self):
        """Test case for get_v2_runs_id_sequencingstats

        """
        pass

    def test_get_v2_runuploadtest(self):
        """Test case for get_v2_runuploadtest

        """
        pass

    def test_get_v2_samples_id_file_upload_info(self):
        """Test case for get_v2_samples_id_file_upload_info

        """
        pass

    def test_get_v2_subjects_id_properties(self):
        """Test case for get_v2_subjects_id_properties

        """
        pass

    def test_get_v2_subjects_id_properties_name(self):
        """Test case for get_v2_subjects_id_properties_name

        """
        pass

    def test_get_v2_subjects_id_properties_name_items(self):
        """Test case for get_v2_subjects_id_properties_name_items

        """
        pass

    def test_get_v2_trash(self):
        """Test case for get_v2_trash

        Get a list of items in the trash  # noqa: E501
        """
        pass

    def test_get_v2_trash_id(self):
        """Test case for get_v2_trash_id

        Get information about an item in the trash  # noqa: E501
        """
        pass

    def test_get_v2_useragreements(self):
        """Test case for get_v2_useragreements

        Get information about agreements visible to the current user  # noqa: E501
        """
        pass

    def test_get_v2_users_current(self):
        """Test case for get_v2_users_current

        Get information about the current user's account  # noqa: E501
        """
        pass

    def test_get_v2_users_current_labtype(self):
        """Test case for get_v2_users_current_labtype

        Is user a wet lab or dry lab user?  # noqa: E501
        """
        pass

    def test_get_v2_users_current_messages(self):
        """Test case for get_v2_users_current_messages

        Get a list of messages that have been sent to the requesting user.  # noqa: E501
        """
        pass

    def test_get_v2_users_current_notifications(self):
        """Test case for get_v2_users_current_notifications

        """
        pass

    def test_get_v2_users_current_properties(self):
        """Test case for get_v2_users_current_properties

        """
        pass

    def test_get_v2_users_current_properties_name(self):
        """Test case for get_v2_users_current_properties_name

        """
        pass

    def test_get_v2_users_current_properties_name_items(self):
        """Test case for get_v2_users_current_properties_name_items

        """
        pass

    def test_get_v2_users_current_subscription(self):
        """Test case for get_v2_users_current_subscription

        Get information about the current user�s subscriptions  # noqa: E501
        """
        pass

    def test_get_v2_users_current_usage(self):
        """Test case for get_v2_users_current_usage

        Get usage statistics for the user  # noqa: E501
        """
        pass

    def test_get_v2_users_id(self):
        """Test case for get_v2_users_id

        Get information about a user  # noqa: E501
        """
        pass

    def test_get_v2_users_id_autodeletionevents(self):
        """Test case for get_v2_users_id_autodeletionevents

        Get a list of auto-deletion events for the specified user.  # noqa: E501
        """
        pass

    def test_get_v2_users_id_messages(self):
        """Test case for get_v2_users_id_messages

        Get a list of messages that have been sent to a specific user.  # noqa: E501
        """
        pass

    def test_get_v2_users_id_notifications(self):
        """Test case for get_v2_users_id_notifications

        """
        pass

    def test_get_v2_users_id_settings(self):
        """Test case for get_v2_users_id_settings

        Get a list of the user's settings  # noqa: E501
        """
        pass

    def test_get_v2_users_id_subscription(self):
        """Test case for get_v2_users_id_subscription

        Get information about a user's subscriptions  # noqa: E501
        """
        pass

    def test_get_v2_users_id_workgroups(self):
        """Test case for get_v2_users_id_workgroups

        Get a list of workgroups the user belongs to  # noqa: E501
        """
        pass

    def test_get_v2_v2migration_status_stepname(self):
        """Test case for get_v2_v2migration_status_stepname

        Get status report on migration   # noqa: E501
        """
        pass

    def test_get_v2_workgroups_id(self):
        """Test case for get_v2_workgroups_id

        Get information about a workgroup  # noqa: E501
        """
        pass

    def test_post_v2_applications_id_workflows(self):
        """Test case for post_v2_applications_id_workflows

        Create or update an analysis workflow  # noqa: E501
        """
        pass

    def test_post_v2_appresults_id_file_upload_info(self):
        """Test case for post_v2_appresults_id_file_upload_info

        """
        pass

    def test_post_v2_appsessions(self):
        """Test case for post_v2_appsessions

        Create a new interactive AppSession with ExecutionStatus Running  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_id(self):
        """Test case for post_v2_appsessions_id

        Update an analysis  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_id_logfiles(self):
        """Test case for post_v2_appsessions_id_logfiles

        Add a log file to a specific analysis  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_id_properties(self):
        """Test case for post_v2_appsessions_id_properties

        Add or update properties of an analysis  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_id_reschedule(self):
        """Test case for post_v2_appsessions_id_reschedule

        Reschedule a workflow  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_id_stop(self):
        """Test case for post_v2_appsessions_id_stop

        Stop an analysis from running  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_track(self):
        """Test case for post_v2_appsessions_track

        Track ICA analyses  # noqa: E501
        """
        pass

    def test_post_v2_appsessions_workflowsessions_track(self):
        """Test case for post_v2_appsessions_workflowsessions_track

        Track workflow sessions  # noqa: E501
        """
        pass

    def test_post_v2_archive(self):
        """Test case for post_v2_archive

        Bulk archive.  # noqa: E501
        """
        pass

    def test_post_v2_biosamples(self):
        """Test case for post_v2_biosamples

        """
        pass

    def test_post_v2_biosamples_bulkupdate(self):
        """Test case for post_v2_biosamples_bulkupdate

        Update the default project of many biosamples  # noqa: E501
        """
        pass

    def test_post_v2_biosamples_id(self):
        """Test case for post_v2_biosamples_id

        Update a Biosample  # noqa: E501
        """
        pass

    def test_post_v2_biosamples_id_aggregation(self):
        """Test case for post_v2_biosamples_id_aggregation

        Update Biosample aggregation  # noqa: E501
        """
        pass

    def test_post_v2_biosamples_id_libraries(self):
        """Test case for post_v2_biosamples_id_libraries

        Create a library for a biosample  # noqa: E501
        """
        pass

    def test_post_v2_datacompress(self):
        """Test case for post_v2_datacompress

        Bulk Data Compression.  # noqa: E501
        """
        pass

    def test_post_v2_datasets(self):
        """Test case for post_v2_datasets

        Create a dataset that doesn't belong in a specific project  # noqa: E501
        """
        pass

    def test_post_v2_datasets_id(self):
        """Test case for post_v2_datasets_id

        Update an existing dataset  # noqa: E501
        """
        pass

    def test_post_v2_datasets_id_copy(self):
        """Test case for post_v2_datasets_id_copy

        Copy a dataset to a project  # noqa: E501
        """
        pass

    def test_post_v2_datasets_id_direct_upload_info(self):
        """Test case for post_v2_datasets_id_direct_upload_info

        """
        pass

    def test_post_v2_datasets_id_file_upload_info(self):
        """Test case for post_v2_datasets_id_file_upload_info

        """
        pass

    def test_post_v2_datasets_id_files(self):
        """Test case for post_v2_datasets_id_files

        """
        pass

    def test_post_v2_icadownloads_create_download_url(self):
        """Test case for post_v2_icadownloads_create_download_url

        """
        pass

    def test_post_v2_icauploads_foldertype_complete_upload(self):
        """Test case for post_v2_icauploads_foldertype_complete_upload

        """
        pass

    def test_post_v2_icauploads_foldertype_direct_upload_info(self):
        """Test case for post_v2_icauploads_foldertype_direct_upload_info

        """
        pass

    def test_post_v2_instrumentdiagnostics(self):
        """Test case for post_v2_instrumentdiagnostics

        """
        pass

    def test_post_v2_instrumentdiagnostics_id(self):
        """Test case for post_v2_instrumentdiagnostics_id

        """
        pass

    def test_post_v2_instruments_errors(self):
        """Test case for post_v2_instruments_errors

        """
        pass

    def test_post_v2_lanes_id(self):
        """Test case for post_v2_lanes_id

        Update a lane  # noqa: E501
        """
        pass

    def test_post_v2_libraries_libraryid_labrequeues(self):
        """Test case for post_v2_libraries_libraryid_labrequeues

        Add a lab requeue request for more yield from a library  # noqa: E501
        """
        pass

    def test_post_v2_librarypools_id(self):
        """Test case for post_v2_librarypools_id

        Update a pool  # noqa: E501
        """
        pass

    def test_post_v2_librarypools_poolid_labrequeues(self):
        """Test case for post_v2_librarypools_poolid_labrequeues

        Add a lab requeue request for more yield from a pool  # noqa: E501
        """
        pass

    def test_post_v2_oauthv1_tokenfromoauthv2(self):
        """Test case for post_v2_oauthv1_tokenfromoauthv2

        """
        pass

    def test_post_v2_oauthv2_token(self):
        """Test case for post_v2_oauthv2_token

        """
        pass

    def test_post_v2_oauthv2_tokenfromapplicationjwt(self):
        """Test case for post_v2_oauthv2_tokenfromapplicationjwt

        """
        pass

    def test_post_v2_oauthv2tokens_userid(self):
        """Test case for post_v2_oauthv2tokens_userid

        """
        pass

    def test_post_v2_preprequests_preprequestid_labrequeues(self):
        """Test case for post_v2_preprequests_preprequestid_labrequeues

        Add a lab requeue request for more yield from a biosample  # noqa: E501
        """
        pass

    def test_post_v2_projects(self):
        """Test case for post_v2_projects

        Create a project by name  # noqa: E501
        """
        pass

    def test_post_v2_projects_id_datasets(self):
        """Test case for post_v2_projects_id_datasets

        Create a dataset within a specific project  # noqa: E501
        """
        pass

    def test_post_v2_publishappsessionstatus(self):
        """Test case for post_v2_publishappsessionstatus

        """
        pass

    def test_post_v2_restore(self):
        """Test case for post_v2_restore

        Bulk restore.  # noqa: E501
        """
        pass

    def test_post_v2_runs(self):
        """Test case for post_v2_runs

        Create a new run  # noqa: E501
        """
        pass

    def test_post_v2_runs_id(self):
        """Test case for post_v2_runs_id

        Update an existing run  # noqa: E501
        """
        pass

    def test_post_v2_runs_id_file_upload_info(self):
        """Test case for post_v2_runs_id_file_upload_info

        """
        pass

    def test_post_v2_runs_id_files(self):
        """Test case for post_v2_runs_id_files

        """
        pass

    def test_post_v2_runs_start(self):
        """Test case for post_v2_runs_start

        Create a new run using GSS  # noqa: E501
        """
        pass

    def test_post_v2_samples_id_file_upload_info(self):
        """Test case for post_v2_samples_id_file_upload_info

        """
        pass

    def test_post_v2_tokens_instruments(self):
        """Test case for post_v2_tokens_instruments

        Creates a Platform JWT token for an instrument  # noqa: E501
        """
        pass

    def test_post_v2_trash_id_restorefromtrash(self):
        """Test case for post_v2_trash_id_restorefromtrash

        Restore an item from the trash back to its active state  # noqa: E501
        """
        pass

    def test_post_v2_unzip(self):
        """Test case for post_v2_unzip

        Bulk Unzip.  # noqa: E501
        """
        pass

    def test_post_v2_useraccounttransfer(self):
        """Test case for post_v2_useraccounttransfer

        User account transfer. Requires Administrator role  # noqa: E501
        """
        pass

    def test_post_v2_useragreements(self):
        """Test case for post_v2_useragreements

        """
        pass

    def test_post_v2_users_current(self):
        """Test case for post_v2_users_current

        """
        pass

    def test_post_v2_users_files(self):
        """Test case for post_v2_users_files

        Upload a file to the user's volume in GDS  # noqa: E501
        """
        pass

    def test_post_v2_users_id_settings(self):
        """Test case for post_v2_users_id_settings

        Update the user's settings   # noqa: E501
        """
        pass

    def test_post_v2_users_id_v2analysisconfigtemplate(self):
        """Test case for post_v2_users_id_v2analysisconfigtemplate

        Change Analysis Configuration Template Feature Enabled for calling user  # noqa: E501
        """
        pass

    def test_post_v2_users_id_v2biosampleregistry(self):
        """Test case for post_v2_users_id_v2biosampleregistry

        Change V2 BioSample Registry Enabled for calling user  # noqa: E501
        """
        pass

    def test_post_v2_validatesignedurl(self):
        """Test case for post_v2_validatesignedurl

        """
        pass

    def test_put_v2_applications_id_qcthresholds(self):
        """Test case for put_v2_applications_id_qcthresholds

        Add or update the QC thresholds applied to an analysis workflow  # noqa: E501
        """
        pass

    def test_put_v2_applications_id_workflowdependencies(self):
        """Test case for put_v2_applications_id_workflowdependencies

        Add or update the workflow dependencies of an analysis workflow  # noqa: E501
        """
        pass

    def test_put_v2_laneqcthresholds(self):
        """Test case for put_v2_laneqcthresholds

        Add or update the QC thresholds applied to lanes  # noqa: E501
        """
        pass

    def test_put_v2_notifications_dismiss(self):
        """Test case for put_v2_notifications_dismiss

        Dismiss a user notification.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
