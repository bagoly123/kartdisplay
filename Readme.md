# Kart Display Read Me

__main__ is the core application and the one that should be executed

__Requests__ Library is __**REQUIRED**__, [installation guide]

__Debug mode__ can be toggled on or of via a bool value at the top of main. If set to True, it will use archived data from an old session. This is for testing functionality.

__Logging__ can now also be enabled/dissabled via a bool value at tge top of main. If enabled, errors, some actions as well as the __racersByName__ dict will be logged into ther respective log files.

| __Error Code__ | __Meaning__ |
| -------------- | ----------- |
| 404 | Racer not in session|
| 408 | No Session Running |
| 444 | Connection Error |

## Note
    As of version 3.3, a segment emulator is being used as the python 3.7 version of the MAX7219 chip library is not compatible with the chips seven segment driver mode. This is to be replaced in a future version with the implementation of support for my custom hardware. Alternatively I wil make a library for the chip myself.

## Change Log:
    V3.6
    Added ablity to enable/dissable logging. Tidied up main, remained functionally the same but is now more readable.

    V3.5
    GetData class Removed, replaced by a static method in SessionData class. Added debug mode. Another Error typo fixed. Bug where exception would be raised if the racer left the session after initialision of main has been fixed.

    V3.4
    Simplifeied json browser in process.py, functionally its the same. Fixed bug where racer lap wouldnt update. Added aditional comments.

    V3.3
    Implemented Segment Emulator

    V3.2
    Fixed issue where memory was flooded with new objects

    V3.1
    First stable build of object orientated archetectured program

## Breakdown Of  "raw" JSON Structure

### Shell (dict)

| messageId | Messages | TransportData |
| --------- | -------- | ------------- |
| int | [Messages] | [TransportData] |

### Messages (list)

| 0 | 
| --------- |
| [Main] |

### Main (dict)

| Hub | Method | Args |
| --------- | -------- | - |
| str | str | [Args]

### Args (list)

| 0 | 
| - |
| [Params] |

### Params (dict)

| Winby | LapsLeft | HeatTypeName | Winners | ScoreboardData | RaceRunning |
| ----- | -------- | ------------ | ------- | -------------- | ----------- |
| str | int/datetime | str | [winners] | [ScoreboardData] | [RaceRunning] |

### raceStatus (dict)

| RaceRunning |
| ----------- |
| bool |

### ScoreboardData (list)

| 0 | 
| --------- |
| [Racer] |

ScoreboardData has an undefined length, based on the number of racers

### Racer (dict)

| CustId | HeatNo | RacerName | AutoNo | AMBTme | LTime | LapNum | BestLTime | Position | GapToLeader | HeatRanking | LastPassedTime | DlTime | DBestLTime | TimeSinceLastPasses | PenaltyFlags |
| ------ | ------ | --------- | ------ | ------ | ----- | ------ | --------- | -------- | ----------- | ----------- | -------------- | ------ | ---------- | ------------------- | ------------ |
| str | int | str | int | float | float | int | float | int | float | int | datetime | relative | relative | relative | bool|

### Winners (dict)

Same as ScoreboardData, when a session ends top 3 Racer tables moved into Winners


[installation guide]: https://realpython.com/python-requests/

