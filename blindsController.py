def control_blinds(blinds_state, keep_track):

    ENABLE_PIN = 19
    MOTOR_PIN1 = 21
    MOTOR_PIN2 = 23

    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)

    pwm = GPIO.PWM(ENABLE_PIN, 100)

    try:

        pwm.start(0)
        while True:
            if blinds_state and keep_track:
                
                keep_track = 0

                # Coboară jaluzelele
                GPIO.output(MOTOR_PIN1, GPIO.HIGH)
                GPIO.output(MOTOR_PIN2, GPIO.LOW)
                

                pwm.ChangeDutyCycle(50)

                time.sleep(2)
            elif not blinds_state and not keep_track:

                keep_track = 1

                # Ridică jaluzelele
                GPIO.output(MOTOR_PIN1, GPIO.LOW)
                GPIO.output(MOTOR_PIN2, GPIO.HIGH)

                for dc in range(100, -1, -5):
                    pwm.ChangeDutyCycle(dc)
                    time.sleep(0.1)

                time.sleep(2)

    except KeyboardInterrupt:
        pwm.stop()