import time
def check_for_alerts():
    #Ellenőrzi az alert_log.txt fájlt
    last_position = 0
    try:
        while True:
            with open("alert_log.txt", "r") as log_file:
                log_file.seek(last_position)
                new_alerts = log_file.readlines()
                last_position = log_file.tell()

                if new_alerts:
                    print("❗ Új riasztás érkezett:")
                    for alert in new_alerts:
                        print(alert, end="")

            time.sleep(5)  # Ellenőrzés 5 másodpercenként
    except KeyboardInterrupt:
        print("\nRiasztási modul leállítva.")

if __name__ == "__main__":
    print("=== Riasztási modul elindítva ===")
    check_for_alerts()


