from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

localized_notification_messages_request_builder = lazy_import('msgraph.generated.device_management.notification_message_templates.item.localized_notification_messages.localized_notification_messages_request_builder')
localized_notification_message_item_request_builder = lazy_import('msgraph.generated.device_management.notification_message_templates.item.localized_notification_messages.item.localized_notification_message_item_request_builder')
send_test_message_request_builder = lazy_import('msgraph.generated.device_management.notification_message_templates.item.microsoft_graph_send_test_message.send_test_message_request_builder')
notification_message_template = lazy_import('msgraph.generated.models.notification_message_template')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class NotificationMessageTemplateItemRequestBuilder():
    """
    Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def localized_notification_messages(self) -> localized_notification_messages_request_builder.LocalizedNotificationMessagesRequestBuilder:
        """
        Provides operations to manage the localizedNotificationMessages property of the microsoft.graph.notificationMessageTemplate entity.
        """
        return localized_notification_messages_request_builder.LocalizedNotificationMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_send_test_message(self) -> send_test_message_request_builder.SendTestMessageRequestBuilder:
        """
        Provides operations to call the sendTestMessage method.
        """
        return send_test_message_request_builder.SendTestMessageRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, notification_message_template_id: Optional[str] = None) -> None:
        """
        Instantiates a new NotificationMessageTemplateItemRequestBuilder and sets the default values.
        Args:
            notificationMessageTemplateId: key: id of notificationMessageTemplate
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/notificationMessageTemplates/{notificationMessageTemplate%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["notificationMessageTemplate%2Did"] = notificationMessageTemplateId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property notificationMessageTemplates for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderGetRequestConfiguration] = None) -> Optional[notification_message_template.NotificationMessageTemplate]:
        """
        The Notification Message Templates.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[notification_message_template.NotificationMessageTemplate]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, notification_message_template.NotificationMessageTemplate, error_mapping)
    
    def localized_notification_messages_by_id(self,id: str) -> localized_notification_message_item_request_builder.LocalizedNotificationMessageItemRequestBuilder:
        """
        Provides operations to manage the localizedNotificationMessages property of the microsoft.graph.notificationMessageTemplate entity.
        Args:
            id: Unique identifier of the item
        Returns: localized_notification_message_item_request_builder.LocalizedNotificationMessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["localizedNotificationMessage%2Did"] = id
        return localized_notification_message_item_request_builder.LocalizedNotificationMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[notification_message_template.NotificationMessageTemplate] = None, request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[notification_message_template.NotificationMessageTemplate]:
        """
        Update the navigation property notificationMessageTemplates in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[notification_message_template.NotificationMessageTemplate]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, notification_message_template.NotificationMessageTemplate, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property notificationMessageTemplates for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Notification Message Templates.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[notification_message_template.NotificationMessageTemplate] = None, request_configuration: Optional[NotificationMessageTemplateItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property notificationMessageTemplates in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderGetQueryParameters():
        """
        The Notification Message Templates.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[NotificationMessageTemplateItemRequestBuilder.NotificationMessageTemplateItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

