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

background_image_request_builder = lazy_import('msgraph.generated.branding.localizations.item.background_image.background_image_request_builder')
banner_logo_request_builder = lazy_import('msgraph.generated.branding.localizations.item.banner_logo.banner_logo_request_builder')
square_logo_request_builder = lazy_import('msgraph.generated.branding.localizations.item.square_logo.square_logo_request_builder')
organizational_branding_localization = lazy_import('msgraph.generated.models.organizational_branding_localization')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class OrganizationalBrandingLocalizationItemRequestBuilder():
    """
    Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
    """
    @property
    def background_image(self) -> background_image_request_builder.BackgroundImageRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return background_image_request_builder.BackgroundImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def banner_logo(self) -> banner_logo_request_builder.BannerLogoRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return banner_logo_request_builder.BannerLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo(self) -> square_logo_request_builder.SquareLogoRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return square_logo_request_builder.SquareLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, organizational_branding_localization_id: Optional[str] = None) -> None:
        """
        Instantiates a new OrganizationalBrandingLocalizationItemRequestBuilder and sets the default values.
        Args:
            organizationalBrandingLocalizationId: key: id of organizationalBrandingLocalization
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/branding/localizations/{organizationalBrandingLocalization%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["organizationalBrandingLocalization%2Did"] = organizationalBrandingLocalizationId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property localizations for branding
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
    
    async def get(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[organizational_branding_localization.OrganizationalBrandingLocalization]:
        """
        Add different branding based on a locale.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding_localization.OrganizationalBrandingLocalization]
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
        return await self.request_adapter.send_async(request_info, organizational_branding_localization.OrganizationalBrandingLocalization, error_mapping)
    
    async def patch(self,body: Optional[organizational_branding_localization.OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[organizational_branding_localization.OrganizationalBrandingLocalization]:
        """
        Update the navigation property localizations in branding
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding_localization.OrganizationalBrandingLocalization]
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
        return await self.request_adapter.send_async(request_info, organizational_branding_localization.OrganizationalBrandingLocalization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property localizations for branding
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
    
    def to_get_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Add different branding based on a locale.
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
    
    def to_patch_request_information(self,body: Optional[organizational_branding_localization.OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property localizations in branding
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
    class OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters():
        """
        Add different branding based on a locale.
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
    class OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OrganizationalBrandingLocalizationItemRequestBuilder.OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

