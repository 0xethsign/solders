from typing import Dict, List, Optional, Sequence, Union

from jsonalias import Json

from solders.account_decoder import UiTokenAmount
from solders.commitment_config import CommitmentConfig
from solders.hash import Hash
from solders.message import MessageHeader
from solders.pubkey import Pubkey
from solders.signature import Signature
from solders.transaction import TransactionVersion, VersionedTransaction

class UiTransactionEncoding:
    Binary: "UiTransactionEncoding"
    Base64: "UiTransactionEncoding"
    Base58: "UiTransactionEncoding"
    Json: "UiTransactionEncoding"
    JsonParsed: "UiTransactionEncoding"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class TransactionDetails:
    Full: "TransactionDetails"
    Signatures: "TransactionDetails"
    None_: "TransactionDetails"
    Accounts: "TransactionDetails"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class TransactionBinaryEncoding:
    Base58: "TransactionBinaryEncoding"
    Base64: "TransactionBinaryEncoding"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class UiCompiledInstruction:
    def __init__(
        self,
        program_id_index: int,
        accounts: bytes,
        data: str,
        stack_height: Optional[int] = None,
    ) -> None: ...
    @property
    def program_id_index(self) -> int: ...
    @property
    def accounts(self) -> bytes: ...
    @property
    def data(self) -> str: ...
    @property
    def stack_height(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiCompiledInstruction": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiCompiledInstruction": ...

class UiAddressTableLookup:
    def __init__(
        self, account_key: Pubkey, writable_indexes: bytes, readonly_indexes: bytes
    ) -> None: ...
    @property
    def account_key(self) -> Pubkey: ...
    @property
    def writable_indexes(self) -> bytes: ...
    @property
    def readonly_indexes(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiAddressTableLookup": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiAddressTableLookup": ...

class UiRawMessage:
    def __init__(
        self,
        header: MessageHeader,
        account_keys: Sequence[Pubkey],
        recent_blockhash: Hash,
        instructions: Sequence[UiCompiledInstruction],
        address_table_lookups: Optional[Sequence[UiAddressTableLookup]] = None,
    ) -> None: ...
    @property
    def header(self) -> MessageHeader: ...
    @property
    def account_keys(self) -> List[Pubkey]: ...
    @property
    def recent_blockhash(self) -> Hash: ...
    @property
    def instructions(self) -> List[UiCompiledInstruction]: ...
    @property
    def address_table_lookups(self) -> Optional[List[UiAddressTableLookup]]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiRawMessage": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiRawMessage": ...

class ParsedAccountSource:
    Transaction: "ParsedAccountSource"
    LookupTable: "ParsedAccountSource"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class ParsedAccount:
    def __init__(
        self,
        pubkey: Pubkey,
        writable: bool,
        signer: bool,
        source: Optional[ParsedAccountSource] = None,
    ) -> None: ...
    @property
    def pubkey(self) -> Pubkey: ...
    @property
    def writable(self) -> bool: ...
    @property
    def signer(self) -> bool: ...
    @property
    def source(self) -> Optional[ParsedAccountSource]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "ParsedAccount": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "ParsedAccount": ...

class ParsedInstruction:
    def __init__(
        self,
        program: str,
        program_id: Pubkey,
        parsed: Dict[str, Json],
        stack_height: Optional[int] = None,
    ) -> None: ...
    @property
    def program(self) -> str: ...
    @property
    def program_id(self) -> Pubkey: ...
    @property
    def parsed(self) -> Dict[str, Json]: ...
    @property
    def stack_height(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "ParsedInstruction": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "ParsedInstruction": ...

class UiPartiallyDecodedInstruction:
    def __init__(
        self,
        program_id: Pubkey,
        accounts: Sequence[Pubkey],
        data: str,
        stack_height: Optional[int] = None,
    ) -> None: ...
    @property
    def program_id(self) -> Pubkey: ...
    @property
    def accounts(self) -> List[Pubkey]: ...
    @property
    def data(self) -> str: ...
    @property
    def stack_height(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiPartiallyDecodedInstruction": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiPartiallyDecodedInstruction": ...

class UiAccountsList:
    def __init__(
        self,
        signatures: Sequence[Signature],
        account_keys: Sequence[ParsedAccount],
    ) -> None: ...
    @property
    def signatures(self) -> List[Signature]: ...
    @property
    def account_keys(self) -> List[ParsedAccount]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiAccountsList": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiAccountsList": ...

class UiParsedMessage:
    def __init__(
        self,
        account_keys: Sequence[ParsedAccount],
        recent_blockhash: Hash,
        instructions: Sequence[UiInstruction],
        address_table_lookups: Optional[Sequence[UiAddressTableLookup]],
    ) -> None: ...
    @property
    def account_keys(self) -> List[ParsedAccount]: ...
    @property
    def recent_blockhash(self) -> Hash: ...
    @property
    def instructions(self) -> List[UiInstruction]: ...
    @property
    def address_table_lookups(self) -> Optional[Sequence[UiAddressTableLookup]]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiParsedMessage": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiParsedMessage": ...

class UiTransaction:
    def __init__(self, signatures: Sequence[Signature], message: UiMessage) -> None: ...
    @property
    def signatures(self) -> List[Signature]: ...
    @property
    def message(self) -> UiMessage: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiTransaction": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiTransaction": ...

class UiInnerInstructions:
    def __init__(self, index: int, instructions: Sequence[UiInstruction]) -> None: ...
    @property
    def index(self) -> int: ...
    @property
    def instructions(self) -> List[UiInstruction]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiInnerInstructions": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiInnerInstructions": ...

class UiLoadedAddresses:
    def __init__(
        self, writable: Sequence[Pubkey], readonly: Sequence[Pubkey]
    ) -> None: ...
    @property
    def writable(self) -> List[Pubkey]: ...
    @property
    def readonly(self) -> List[Pubkey]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiLoadedAddresses": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiLoadedAddresses": ...

class UiTransactionTokenBalance:
    def __init__(
        self,
        account_index: int,
        mint: Pubkey,
        ui_token_amount: UiTokenAmount,
        owner: Optional[Pubkey],
        program_id: Optional[Pubkey],
    ) -> None: ...
    @property
    def account_index(self) -> int: ...
    @property
    def mint(self) -> Pubkey: ...
    @property
    def ui_token_amount(self) -> UiTokenAmount: ...
    @property
    def owner(self) -> Optional[Pubkey]: ...
    @property
    def program_id(self) -> Optional[Pubkey]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiTransactionTokenBalance": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiTransactionTokenBalance": ...

class RewardType:
    Fee: "RewardType"
    Rent: "RewardType"
    Staking: "RewardType"
    Voting: "RewardType"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class TransactionReturnData:
    def __init__(self, program_id: Pubkey, data: Sequence[int]) -> None: ...
    @property
    def program_id(self) -> Pubkey: ...
    @property
    def data(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "TransactionReturnData": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "TransactionReturnData": ...

class UiTransactionStatusMeta:
    def __init__(
        self,
        err: Optional[TransactionErrorType],
        fee: int,
        pre_balances: Sequence[int],
        post_balances: Sequence[int],
        inner_instructions: Optional[Sequence[UiInnerInstructions]] = None,
        log_messages: Optional[Sequence[str]] = None,
        pre_token_balances: Optional[Sequence[UiTransactionTokenBalance]] = None,
        post_token_balances: Optional[Sequence[UiTransactionTokenBalance]] = None,
        rewards: Optional[Sequence[Reward]] = None,
        loaded_addresses: Optional[UiLoadedAddresses] = None,
        return_data: Optional[TransactionReturnData] = None,
        compute_units_consumed: Optional[int] = None,
    ) -> None: ...
    @property
    def err(self) -> Optional[TransactionErrorType]: ...
    @property
    def fee(self) -> int: ...
    @property
    def pre_balances(self) -> List[int]: ...
    @property
    def post_balances(self) -> List[int]: ...
    @property
    def inner_instructions(self) -> Optional[List[UiInnerInstructions]]: ...
    @property
    def log_messages(self) -> Optional[List[str]]: ...
    @property
    def pre_token_balances(self) -> Optional[List[UiTransactionTokenBalance]]: ...
    @property
    def post_token_balances(self) -> Optional[List[UiTransactionTokenBalance]]: ...
    @property
    def rewards(self) -> Optional[List[Reward]]: ...
    @property
    def loaded_addresses(self) -> Optional[UiLoadedAddresses]: ...
    @property
    def return_data(self) -> Optional[TransactionReturnData]: ...
    @property
    def compute_units_consumed(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "UiTransactionStatusMeta": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "UiTransactionStatusMeta": ...

class EncodedTransactionWithStatusMeta:
    def __init__(
        self,
        transaction: EncodedVersionedTransaction,
        meta: Optional[UiTransactionStatusMeta],
        version: Optional[TransactionVersion],
    ) -> None: ...
    @property
    def transaction(self) -> EncodedVersionedTransaction: ...
    @property
    def meta(self) -> Optional[UiTransactionStatusMeta]: ...
    @property
    def version(self) -> Optional[TransactionVersion]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "EncodedTransactionWithStatusMeta": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "EncodedTransactionWithStatusMeta": ...

class InstructionErrorCustom:
    def __init__(self, code: int) -> None: ...
    @property
    def code(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "InstructionErrorCustom": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "InstructionErrorCustom": ...

class InstructionErrorBorshIO:
    def __init__(self, value: str) -> None: ...
    @property
    def value(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "InstructionErrorBorshIO": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "InstructionErrorBorshIO": ...

class InstructionErrorFieldless:
    GenericError: "InstructionErrorFieldless"
    InvalidArgument: "InstructionErrorFieldless"
    InvalidInstructionData: "InstructionErrorFieldless"
    InvalidAccountData: "InstructionErrorFieldless"
    AccountDataTooSmall: "InstructionErrorFieldless"
    InsufficientFunds: "InstructionErrorFieldless"
    IncorrectProgramId: "InstructionErrorFieldless"
    MissingRequiredSignature: "InstructionErrorFieldless"
    AccountAlreadyInitialized: "InstructionErrorFieldless"
    UninitializedAccount: "InstructionErrorFieldless"
    UnbalancedInstruction: "InstructionErrorFieldless"
    ModifiedProgramId: "InstructionErrorFieldless"
    ExternalAccountLamportSpend: "InstructionErrorFieldless"
    ExternalAccountDataModified: "InstructionErrorFieldless"
    ReadonlyLamportChange: "InstructionErrorFieldless"
    ReadonlyDataModified: "InstructionErrorFieldless"
    DuplicateAccountIndex: "InstructionErrorFieldless"
    ExecutableModified: "InstructionErrorFieldless"
    RentEpochModified: "InstructionErrorFieldless"
    NotEnoughAccountKeys: "InstructionErrorFieldless"
    AccountDataSizeChanged: "InstructionErrorFieldless"
    AccountNotExecutable: "InstructionErrorFieldless"
    AccountBorrowFailed: "InstructionErrorFieldless"
    AccountBorrowOutstanding: "InstructionErrorFieldless"
    DuplicateAccountOutOfSync: "InstructionErrorFieldless"
    InvalidError: "InstructionErrorFieldless"
    ExecutableDataModified: "InstructionErrorFieldless"
    ExecutableLamportChange: "InstructionErrorFieldless"
    ExecutableAccountNotRentExempt: "InstructionErrorFieldless"
    UnsupportedProgramId: "InstructionErrorFieldless"
    CallDepth: "InstructionErrorFieldless"
    MissingAccount: "InstructionErrorFieldless"
    ReentrancyNotAllowed: "InstructionErrorFieldless"
    MaxSeedLengthExceeded: "InstructionErrorFieldless"
    InvalidSeeds: "InstructionErrorFieldless"
    InvalidRealloc: "InstructionErrorFieldless"
    ComputationalBudgetExceeded: "InstructionErrorFieldless"
    PrivilegeEscalation: "InstructionErrorFieldless"
    ProgramEnvironmentSetupFailure: "InstructionErrorFieldless"
    ProgramFailedToComplete: "InstructionErrorFieldless"
    ProgramFailedToCompile: "InstructionErrorFieldless"
    Immutable: "InstructionErrorFieldless"
    IncorrectAuthority: "InstructionErrorFieldless"
    AccountNotRentExempt: "InstructionErrorFieldless"
    InvalidAccountOwner: "InstructionErrorFieldless"
    ArithmeticOverflow: "InstructionErrorFieldless"
    UnsupportedSysvar: "InstructionErrorFieldless"
    IllegalOwner: "InstructionErrorFieldless"
    MaxAccountsDataAllocationsExceeded: "InstructionErrorFieldless"
    ActiveVoteAccountClose: "InstructionErrorFieldless"
    MaxInstructionTraceLengthExceeded: "InstructionErrorFieldless"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class TransactionErrorInstructionError:
    def __init__(self, index: int, err: InstructionErrorType) -> None: ...
    @property
    def index(self) -> int: ...
    @property
    def err(self) -> InstructionErrorType: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "TransactionErrorInstructionError": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "TransactionErrorInstructionError": ...

class TransactionErrorDuplicateInstruction:
    def __init__(self, index: int) -> None: ...
    @property
    def index(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "TransactionErrorDuplicateInstruction": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "TransactionErrorDuplicateInstruction": ...

class TransactionErrorInsufficientFundsForRent:
    account_index: int
    def __init__(self, account_index: int) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "TransactionErrorInsufficientFundsForRent": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "TransactionErrorInsufficientFundsForRent": ...

class TransactionErrorFieldless:
    AccountInUse: "TransactionErrorFieldless"
    AccountLoadedTwice: "TransactionErrorFieldless"
    AccountNotFound: "TransactionErrorFieldless"
    ProgramAccountNotFound: "TransactionErrorFieldless"
    InsufficientFundsForFee: "TransactionErrorFieldless"
    InvalidAccountForFee: "TransactionErrorFieldless"
    AlreadyProcessed: "TransactionErrorFieldless"
    BlockhashNotFound: "TransactionErrorFieldless"
    CallChainTooDeep: "TransactionErrorFieldless"
    MissingSignatureForFee: "TransactionErrorFieldless"
    InvalidAccountIndex: "TransactionErrorFieldless"
    SignatureFailure: "TransactionErrorFieldless"
    InvalidProgramForExecution: "TransactionErrorFieldless"
    SanitizeFailure: "TransactionErrorFieldless"
    ClusterMaintenance: "TransactionErrorFieldless"
    AccountBorrowOutstanding: "TransactionErrorFieldless"
    WouldExceedMaxBlockCostLimit: "TransactionErrorFieldless"
    UnsupportedVersion: "TransactionErrorFieldless"
    InvalidWritableAccount: "TransactionErrorFieldless"
    WouldExceedMaxAccountCostLimit: "TransactionErrorFieldless"
    WouldExceedAccountDataBlockLimit: "TransactionErrorFieldless"
    TooManyAccountLocks: "TransactionErrorFieldless"
    AddressLookupTableNotFound: "TransactionErrorFieldless"
    InvalidAddressLookupTableOwner: "TransactionErrorFieldless"
    InvalidAddressLookupTableData: "TransactionErrorFieldless"
    InvalidAddressLookupTableIndex: "TransactionErrorFieldless"
    InvalidRentPayingAccount: "TransactionErrorFieldless"
    WouldExceedMaxVotefCostLimit: "TransactionErrorFieldless"
    WouldExceedAccountDataTotalLimit: "TransactionErrorFieldless"
    MaxLoadedAccountsDataSizeExceeded: "TransactionErrorFieldless"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

UiParsedInstruction = Union[ParsedInstruction, UiPartiallyDecodedInstruction]
UiInstruction = Union[UiParsedInstruction, UiCompiledInstruction]
UiMessage = Union[UiParsedMessage, UiRawMessage]
EncodedVersionedTransaction = Union[VersionedTransaction, UiTransaction, UiAccountsList]
InstructionErrorType = Union[
    InstructionErrorFieldless,
    InstructionErrorCustom,
    InstructionErrorBorshIO,
]
TransactionErrorType = Union[
    TransactionErrorFieldless,
    TransactionErrorInstructionError,
    TransactionErrorDuplicateInstruction,
    TransactionErrorInsufficientFundsForRent,
]

class Reward:
    def __init__(
        self,
        pubkey: Pubkey,
        lamports: int,
        post_balance: int,
        reward_type: Optional[RewardType] = None,
        commission: Optional[int] = None,
    ) -> None: ...
    @property
    def pubkey(self) -> Pubkey: ...
    @property
    def lamports(self) -> int: ...
    @property
    def post_balance(self) -> int: ...
    @property
    def reward_type(self) -> Optional[RewardType]: ...
    @property
    def commission(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "Reward": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Reward": ...

class TransactionConfirmationStatus:
    Processed: "TransactionConfirmationStatus"
    Confirmed: "TransactionConfirmationStatus"
    Finalized: "TransactionConfirmationStatus"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class TransactionStatus:
    def __init__(
        self,
        slot: int,
        confirmations: Optional[int] = None,
        status: Optional[TransactionErrorType] = None,
        err: Optional[TransactionErrorType] = None,
        confirmation_status: Optional[TransactionConfirmationStatus] = None,
    ) -> None: ...
    @property
    def slot(self) -> int: ...
    @property
    def confirmations(self) -> Optional[int]: ...
    @property
    def status(self) -> Optional[TransactionErrorType]: ...
    @property
    def err(self) -> Optional[TransactionErrorType]: ...
    @property
    def confirmation_status(self) -> Optional[TransactionConfirmationStatus]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "TransactionStatus": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "TransactionStatus": ...
    def satisfies_commitment(self, commitment_config: CommitmentConfig) -> bool: ...
    def get_confirmation_status(self) -> TransactionConfirmationStatus: ...

class EncodedConfirmedTransactionWithStatusMeta:
    def __init__(
        self,
        slot: int,
        transaction: EncodedTransactionWithStatusMeta,
        block_time: Optional[int] = None,
    ) -> None: ...
    @property
    def slot(self) -> int: ...
    @property
    def transaction(self) -> EncodedTransactionWithStatusMeta: ...
    @property
    def block_time(self) -> Optional[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(
        self,
        other: object,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw: bytes) -> "EncodedConfirmedTransactionWithStatusMeta": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "EncodedConfirmedTransactionWithStatusMeta": ...

class UiConfirmedBlock:
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
    def from_json(raw: str) -> UiConfirmedBlock: ...
    @staticmethod
    def from_bytes(data: bytes) -> UiConfirmedBlock: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...
