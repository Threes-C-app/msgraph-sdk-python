from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class NpvPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new npvPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The rate property
        self._rate: Optional[json.Json] = None
        # The values property
        self._values: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NpvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NpvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NpvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def rate(self,) -> Optional[json.Json]:
        """
        Gets the rate property value. The rate property
        Returns: Optional[json.Json]
        """
        return self._rate
    
    @rate.setter
    def rate(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the rate property value. The rate property
        Args:
            value: Value to set for the rate property.
        """
        self._rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. The values property
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. The values property
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

