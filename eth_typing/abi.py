from typing import (
    Any,
    Literal,
    Sequence,
    Tuple,
    TypedDict,
    Union,
)

from typing_extensions import (
    deprecated,
)

from eth_typing.encoding import (
    HexStr,
)

TypeStr = str
"""String representation of a data type."""
Decodable = Union[bytes, bytearray]
"""Binary data to be decoded."""

ABI_COMPONENT_DEPRECATION_MSG = "`{0}` is deprecated, use `ABIComponent` instead."


@deprecated(ABI_COMPONENT_DEPRECATION_MSG.format("ABIEventComponent"))
class ABIEventComponent(TypedDict, total=False):
    """
    TypedDict to represent the `ABI` for nested event parameters.
    Used as a component of `ABIEventParam`.
    """

    components: Sequence["ABIEventComponent"]
    """List of nested event parameters for tuple event ABI types."""
    name: str
    """Name of the event parameter."""
    type: str
    """Type of the event parameter."""


@deprecated(ABI_COMPONENT_DEPRECATION_MSG.format("ABIEventParam"))
class ABIEventParam(TypedDict, total=False):
    """
    TypedDict to represent the `ABI` for event parameters.
    """

    indexed: bool
    """If True, event parameter can be used as a topic filter."""
    components: Sequence["ABIEventComponent"]
    """List of nested event parameters for tuple event ABI types."""
    name: str
    """Name of the event parameter."""
    type: str
    """Type of the event parameter."""


class ABIComponent(TypedDict):
    """
    TypedDict representing an `ABIElement` component.
    """

    components: Sequence["ABIComponent"]
    """List of nested `ABI` components for ABI types."""
    name: str
    """Name of the component."""
    type: str
    """Type of the component."""


class ABIComponentIndexed(ABIComponent):
    """
    TypedDict representing an indexed `ABIElement` component.
    """

    indexed: bool
    """If True, component can be used as a topic filter."""


class ABIEvent(TypedDict, total=False):
    """
    TypedDict to represent the `ABI` for an event.
    """

    anonymous: bool
    """If True, event is anonymous. Cannot filter the event by name."""
    inputs: Sequence["ABIComponent"]
    """Input components for the event."""
    name: str
    """Event name identifier."""
    type: Literal["event"]
    """Event ABI type."""


@deprecated(ABI_COMPONENT_DEPRECATION_MSG.format("ABIFunctionComponent"))
class ABIFunctionComponent(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for nested function parameters.
    Used as a component of `ABIFunctionParam`.
    """

    components: Sequence["ABIFunctionComponent"]
    """List of nested function parameters for tuple function ABI types."""
    name: str
    """Name of the function parameter."""
    type: str
    """Type of the function parameter."""


@deprecated(ABI_COMPONENT_DEPRECATION_MSG.format("ABIFunctionParam"))
class ABIFunctionParam(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for function parameters.
    """

    components: Sequence["ABIFunctionComponent"]
    """List of nested function parameters for tuple function ABI types."""
    name: str
    """Name of the function parameter."""
    type: str
    """Type of the function parameter."""


class ABIFunctionType(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for all function types.

    This is the base type for functions.
    Please use ABIFunction, ABIConstructor, ABIFallback or ABIReceive instead.
    """

    stateMutability: Literal["pure", "view", "nonpayable", "payable"]
    """State mutability of the constructor."""
    payable: bool
    """
    Contract is payable to receive ether on deployment.
    Deprecated in favor of stateMutability payable and nonpayable.
    """
    constant: bool
    """
    Function is constant and does not change state.
    Deprecated in favor of stateMutability pure and view.
    """


class ABIFunction(ABIFunctionType, total=False):
    """
    TypedDict representing the `ABI` for a function.
    """

    type: Literal["function"]
    """Type of the function."""
    inputs: Sequence["ABIComponent"]
    """Function input components."""
    name: str
    """Name of the function."""
    outputs: Sequence["ABIComponent"]
    """Function output components."""


class ABIConstructor(ABIFunctionType, total=False):
    """
    TypedDict representing the `ABI` for a constructor function.
    """

    type: Literal["constructor"]
    """Type of the constructor function."""
    inputs: Sequence["ABIComponent"]
    """Function input components."""


class ABIFallback(ABIFunctionType, total=False):
    """
    TypedDict representing the `ABI` for a fallback function.
    """

    type: Literal["fallback"]
    """Type of the fallback function."""


class ABIReceive(ABIFunctionType, total=False):
    """
    TypedDict representing the `ABI` for a receive function.
    """

    type: Literal["receive"]
    """Type of the receive function."""


class ABIFunctionInfo(TypedDict, total=False):
    """
    TypedDict to represent an `ABIFunction` with the function selector and
    corresponding arguments.
    """

    abi: ABIFunction
    """ABI for the function interface."""
    selector: HexStr
    """Solidity Function selector sighash."""
    arguments: Tuple[Any, ...]
    """Function input components."""


class ABIError(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for an error.
    """

    type: Literal["error"]
    """Type of the error."""
    inputs: Sequence["ABIComponent"]
    """Error input components."""
    name: str
    """Name of the error."""


ABIElement = Union[
    ABIFunction, ABIConstructor, ABIFallback, ABIReceive, ABIEvent, ABIError
]
"""Base type for `ABIFunction` and `ABIEvent` types."""
ABI = Sequence[ABIElement]
"""
List of components representing function and event interfaces
(elements of an ABI).
"""
