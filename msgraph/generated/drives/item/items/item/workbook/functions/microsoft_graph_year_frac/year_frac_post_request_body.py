from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class YearFracPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def basis(self,) -> Optional[json.Json]:
        """
        Gets the basis property value. The basis property
        Returns: Optional[json.Json]
        """
        return self._basis
    
    @basis.setter
    def basis(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the basis property value. The basis property
        Args:
            value: Value to set for the basis property.
        """
        self._basis = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new yearFracPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The basis property
        self._basis: Optional[json.Json] = None
        # The endDate property
        self._end_date: Optional[json.Json] = None
        # The startDate property
        self._start_date: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> YearFracPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: YearFracPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return YearFracPostRequestBody()
    
    @property
    def end_date(self,) -> Optional[json.Json]:
        """
        Gets the endDate property value. The endDate property
        Returns: Optional[json.Json]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the endDate property value. The endDate property
        Args:
            value: Value to set for the end_date property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "endDate": lambda n : setattr(self, 'end_date', n.get_object_value(json.Json)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("endDate", self.end_date)
        writer.write_object_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date(self,) -> Optional[json.Json]:
        """
        Gets the startDate property value. The startDate property
        Returns: Optional[json.Json]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startDate property value. The startDate property
        Args:
            value: Value to set for the start_date property.
        """
        self._start_date = value
    

