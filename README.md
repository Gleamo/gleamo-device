# Gleamo Raspberry Pi Code



Gleamo:
  Has a STATE

Scheduler:

  Knows which command is current, next, etc.
  Handles queuing commands and interupts

Executor:

  Knows how to apply a Command on the current state
  Handles animating between states.

PollingService

HardwareService

Command:

  Animation offset start
  Animation duration
  Animation offset end
  Color
  BuzzPattern

State:


Gleamo is at STATE(INITIAL)

The PollingService receives a set of Commands(A, B, C)
The PollingService gives the Commands(A, B, C) to the Scheduler

The Scheduler is set to run every second. It determines
that Command A should be tweened to by T_A time.

The Scheduler, every tick, tells the Executor, Tween_To
Command A from the STATE. The Scheduler recieves a new STATE
and applies it to Gleamo via the HardwareService

The HardwareService takes care of translating a STATE to
the PIN commands
