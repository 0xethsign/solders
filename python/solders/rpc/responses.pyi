from __future__ import annotations
from typing import Sequence, List, Optional, TypeVar, Union, Tuple, Dict
from solders.hash import Hash
from solders.account import Account, AccountJSON
from solders.transaction_status import (
    EncodedTransactionWithStatusMeta,
    Reward,
)
from solders.signature import Signature
from solders.pubkey import Pubkey
from solders.epoch_schedule import EpochSchedule
from solders.rpc.errors import RpcCustomError
from solders.transaction import VersionedTransaction
from solders.transaction_status import TransactionErrorType, TransactionReturnData

class RpcResponseContext:
    slot: int
    api_version: Optional[str]
    def __init__(self, slot: int, api_version: Optional[str] = None) -> None: ...

class RpcError:
    code: int
    message: str
    data: Optional[RpcCustomError]
    def __init__(
        self, code: int, message: str, data: Optional[RpcCustomError] = None
    ) -> None: ...

T = TypeVar("T")
Resp = Union[RpcError, T]

class GetAccountInfoResp:
    context: RpcResponseContext
    value: Optional[Account]
    def __init__(
        self, value: Optional[Account], context: RpcResponseContext
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetAccountInfoResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetAccountInfoResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetAccountInfoJsonParsedResp:
    context: RpcResponseContext
    value: Optional[AccountJSON]
    def __init__(
        self, value: Optional[AccountJSON], context: RpcResponseContext
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetAccountInfoJsonParsedResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetAccountInfoJsonParsedResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBalanceResp:
    context: RpcResponseContext
    value: int
    def __init__(self, value: int, context: RpcResponseContext) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBalanceResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBalanceResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockCommitmentResp:
    commitment: Optional[List[int]]
    total_stake: int
    def __init__(
        self, commitment: Optional[Sequence[int]], total_stake: int
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockCommitmentResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockCommitmentResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockHeightResp:
    def __init__(self, height: int) -> None: ...
    @property
    def height(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockHeightResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockHeightResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcBlockProductionRange:
    def __init__(
        self,
        first_slot: int,
        last_slot: int,
    ) -> None: ...
    @property
    def first_slot(self) -> int: ...
    @property
    def last_slot(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> RpcBlockProductionRange: ...
    @staticmethod
    def from_bytes(data: bytes) -> RpcBlockProductionRange: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcBlockProduction:
    def __init__(
        self,
        by_identity: Dict[Pubkey, Tuple[int, int]],
        range: RpcBlockProductionRange,
    ) -> None: ...
    @property
    def by_identity(self) -> Dict[Pubkey, Tuple[int, int]]: ...
    @property
    def range(self) -> RpcBlockProductionRange: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> RpcBlockProduction: ...
    @staticmethod
    def from_bytes(data: bytes) -> RpcBlockProduction: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockProductionResp:
    value: RpcBlockProduction
    context: RpcResponseContext
    def __init__(
        self, value: RpcBlockProduction, context: RpcResponseContext
    ) -> None: ...
    @property
    def height(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockProductionResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockProductionResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockResp:
    previous_blockhash: Hash
    blockhash: Hash
    parent_slot: int
    transactions: Optional[List[EncodedTransactionWithStatusMeta]]
    signatures: Optional[List[Signature]]
    rewards: Optional[List[Reward]]
    block_time: Optional[int]
    block_height: Optional[int]
    def __init__(
        self,
        previous_blockhash: Hash,
        blockhash: Hash,
        parent_slot: int,
        transactions: Optional[Sequence[EncodedTransactionWithStatusMeta]] = None,
        signatures: Optional[Sequence[Signature]] = None,
        rewards: Optional[Sequence[Reward]] = None,
        block_time: Optional[int] = None,
        block_height: Optional[int] = None,
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlocksResp:
    def __init__(self, blocks: List[int]) -> None: ...
    @property
    def blocks(self) -> List[int]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlocksResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlocksResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockTimeResp:
    def __init__(self, time: Optional[int] = None) -> None: ...
    @property
    def time(self) -> Optional[int]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockTimeResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockTimeResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcContactInfo:
    pubkey: Pubkey
    gossip: Optional[str]
    tpu: Optional[str]
    rpc: Optional[str]
    version: Optional[str]
    feature_set: Optional[int]
    shred_version: Optional[int]
    def __init__(
        self,
        pubkey: Pubkey,
        gossip: Optional[str] = None,
        tpu: Optional[str] = None,
        rpc: Optional[str] = None,
        version: Optional[str] = None,
        feature_set: Optional[int] = None,
        shred_version: Optional[int] = None,
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> RpcContactInfo: ...
    @staticmethod
    def from_bytes(data: bytes) -> RpcContactInfo: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetClusterNodesResp:
    def __init__(self, nodes: Sequence[RpcContactInfo]) -> None: ...
    @property
    def nodes(self) -> List[RpcContactInfo]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetClusterNodesResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetClusterNodesResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class EpochInfo:
    epoch: int
    slot_index: int
    slots_in_epoch: int
    absolute_slot: int
    block_height: int
    transaction_count: Optional[int]
    def __init__(
        self,
        epoch: int,
        slot_index: int,
        slots_in_epoch: int,
        absolute_slot: int,
        block_height: int,
        transaction_count: Optional[int] = None,
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> EpochInfo: ...
    @staticmethod
    def from_bytes(data: bytes) -> EpochInfo: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetEpochInfoResp:
    def __init__(self, info: EpochInfo) -> None: ...
    @property
    def info(self) -> EpochInfo: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetEpochInfoResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetEpochInfoResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetEpochScheduleResp:
    def __init__(self, schedule: EpochSchedule) -> None: ...
    @property
    def schedule(self) -> EpochSchedule: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetEpochScheduleResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetEpochScheduleResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetFeeForMessageResp:
    context: RpcResponseContext
    value: Optional[int]
    def __init__(self, value: Optional[int], context: RpcResponseContext) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetFeeForMessageResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetFeeForMessageResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetFirstAvailableBlockResp:
    def __init__(self, slot: int) -> None: ...
    @property
    def slot(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetFirstAvailableBlockResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetFirstAvailableBlockResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetGenesisHashResp:
    def __init__(self, value: Hash) -> None: ...
    @property
    def value(self) -> Hash: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetGenesisHashResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetGenesisHashResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetHealthResp:
    def __init__(self, health: str) -> None: ...
    @property
    def health(self) -> str: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetHealthResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetHealthResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcSimulateTransactionResult:
    err: Optional[TransactionErrorType]
    logs: Optional[List[str]]
    accounts: Optional[List[Optional[Account]]]
    units_consumed: Optional[int]
    return_data: Optional[TransactionReturnData]

    def __init__(
        self,
        err: Optional[TransactionErrorType] = None,
        logs: Optional[Sequence[str]] = None,
        accounts: Optional[Sequence[Optional[Account]]] = None,
        units_consumed: Optional[int] = None,
        return_data: Optional[TransactionReturnData] = None,
    ) -> None: ...
