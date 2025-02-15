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

app_role_assignment_request_builder = lazy_import('msgraph.generated.me.owned_devices.item.microsoft_graph_app_role_assignment.app_role_assignment_request_builder')
device_request_builder = lazy_import('msgraph.generated.me.owned_devices.item.microsoft_graph_device.device_request_builder')
endpoint_request_builder = lazy_import('msgraph.generated.me.owned_devices.item.microsoft_graph_endpoint.endpoint_request_builder')
directory_object = lazy_import('msgraph.generated.models.directory_object')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DirectoryObjectItemRequestBuilder():
    """
    Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
    """
    @property
    def microsoft_graph_app_role_assignment(self) -> app_role_assignment_request_builder.AppRoleAssignmentRequestBuilder:
        """
        Casts the previous resource to appRoleAssignment.
        """
        return app_role_assignment_request_builder.AppRoleAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_device(self) -> device_request_builder.DeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        return device_request_builder.DeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_endpoint(self) -> endpoint_request_builder.EndpointRequestBuilder:
        """
        Casts the previous resource to endpoint.
        """
        return endpoint_request_builder.EndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, directory_object_id: Optional[str] = None) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        Args:
            directoryObjectId: key: id of directoryObject
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/ownedDevices/{directoryObject%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["directoryObject%2Did"] = directoryObjectId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[DirectoryObjectItemRequestBuilderGetRequestConfiguration] = None) -> Optional[directory_object.DirectoryObject]:
        """
        Devices that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[directory_object.DirectoryObject]
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
        return await self.request_adapter.send_async(request_info, directory_object.DirectoryObject, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DirectoryObjectItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Devices that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
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
    
    @dataclass
    class DirectoryObjectItemRequestBuilderGetQueryParameters():
        """
        Devices that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
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
    class DirectoryObjectItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DirectoryObjectItemRequestBuilder.DirectoryObjectItemRequestBuilderGetQueryParameters] = None

    

