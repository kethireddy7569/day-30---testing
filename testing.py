# import csv
# import json
# import os
# import subprocess
# import sys
# import time
# from datetime import datetime, timezone

# TEST_DURATION_MINUTES = 120
# TEST_INTERVAL_SECONDS = 60

# RESULT_FOLDER = "milestone_results"

# CSV_FILE = os.path.join(
#     RESULT_FOLDER,
#     "milestone_metrics.csv"
# )

# JSON_FILE = os.path.join(
#     RESULT_FOLDER,
#     "milestone_summary.json"
# )

# os.makedirs(RESULT_FOLDER, exist_ok=True)



# def get_time():
#     return datetime.now(timezone.utc).isoformat()

# def run_application():

#     start_time = time.time()

#     try:

#         result = subprocess.run(
#             [sys.executable, "optimization.py"],
#             capture_output=True,
#             text=True,
#             timeout=TEST_INTERVAL_SECONDS
#         )

#         processing_time = round(
#             time.time() - start_time,
#             2
#         )

#         if result.returncode == 0:

#             status = "SUCCESS"

#         else:

#             status = "FAILED"

#         return {
#             "status": status,
#             "processing_time": processing_time,
#             "exit_code": result.returncode,
#             "output": result.stdout,
#             "error": result.stderr
#         }

#     except subprocess.TimeoutExpired:

#         processing_time = round(
#             time.time() - start_time,
#             2
#         )

#         return {
#             "status": "TIMEOUT",
#             "processing_time": processing_time,
#             "exit_code": -1,
#             "output": "",
#             "error": "Application exceeded test interval."
#         }

#     except Exception as error:

#         return {
#             "status": "ERROR",
#             "processing_time": 0,
#             "exit_code": -1,
#             "output": "",
#             "error": str(error)
#         }

# def save_csv(results):

#     with open(
#         CSV_FILE,
#         "w",
#         newline="",
#         encoding="utf-8"
#     ) as file:

#         writer = csv.DictWriter(
#             file,
#             fieldnames=[
#                 "cycle",
#                 "timestamp",
#                 "status",
#                 "processing_time_seconds",
#                 "exit_code"
#             ]
#         )

#         writer.writeheader()

#         for item in results:

#             writer.writerow({
#                 "cycle": item["cycle"],
#                 "timestamp": item["timestamp"],
#                 "status": item["status"],
#                 "processing_time_seconds":
#                     item["processing_time_seconds"],
#                 "exit_code": item["exit_code"]
#             })


# def main():

#     print("=" * 60)
#     print("DAY 30 - MILESTONE TESTING")
#     print("=" * 60)

#     print(
#         f"Test Duration : "
#         f"{TEST_DURATION_MINUTES} minutes"
#     )

#     print(
#         f"Test Interval : "
#         f"{TEST_INTERVAL_SECONDS} seconds"
#     )

#     print("=" * 60)

#     results = []

#     start_time = get_time()

#     test_start = time.time()

#     cycle = 0

#     while (
#         time.time() - test_start
#         < TEST_DURATION_MINUTES * 60
#     ):

#         cycle += 1

#         print()
#         print(
#             f"Running test cycle {cycle}..."
#         )

#         result = run_application()

#         record = {
#             "cycle": cycle,
#             "timestamp": get_time(),
#             "status": result["status"],
#             "processing_time_seconds":
#                 result["processing_time"],
#             "exit_code":
#                 result["exit_code"]
#         }

#         results.append(record)

#         print(
#             f"Status     : {result['status']}"
#         )

#         print(
#             f"Processing : "
#             f"{result['processing_time']} seconds"
#         )

#         print(
#             f"Exit code  : {result['exit_code']}"
#         )

#         if result["error"]:

#             print(
#                 f"Error      : "
#                 f"{result['error']}"
#             )

#         save_csv(results)

#         # Wait before next cycle
#         remaining = (
#             TEST_DURATION_MINUTES * 60
#             - (time.time() - test_start)
#         )

#         if remaining <= 0:
#             break

#         time.sleep(
#             min(
#                 TEST_INTERVAL_SECONDS,
#                 remaining
#             )
#         )

#     end_time = get_time()

#     total = len(results)

#     successful = sum(
#         1
#         for item in results
#         if item["status"] == "SUCCESS"
#     )

#     failed = total - successful

#     success_rate = (
#         (successful / total) * 100
#         if total > 0
#         else 0
#     )

#     average_time = (
#         sum(
#             item["processing_time_seconds"]
#             for item in results
#         ) / total
#         if total > 0
#         else 0
#     )

#     summary = {

#         "test_name":
#             "Day 30 - Milestone Testing",

#         "test_duration_minutes":
#             TEST_DURATION_MINUTES,

#         "start_time":
#             start_time,

#         "end_time":
#             end_time,

#         "total_cycles":
#             total,

#         "successful_cycles":
#             successful,

#         "failed_cycles":
#             failed,

#         "success_rate_percent":
#             round(success_rate, 2),

#         "average_processing_time_seconds":
#             round(average_time, 2),

#         "overall_status":
#             "PASSED"
#             if failed == 0
#             else "COMPLETED_WITH_ERRORS"
#     }

#     with open(
#         JSON_FILE,
#         "w",
#         encoding="utf-8"
#     ) as file:

#         json.dump(
#             summary,
#             file,
#             indent=4
#         )

#     print()
#     print("=" * 60)
#     print("MILESTONE TEST COMPLETED")
#     print("=" * 60)

#     print(
#         f"Total Cycles  : {total}"
#     )

#     print(
#         f"Successful     : {successful}"
#     )

#     print(
#         f"Failed         : {failed}"
#     )

#     print(
#         f"Success Rate   : "
#         f"{round(success_rate, 2)}%"
#     )

#     print(
#         f"Average Time   : "
#         f"{round(average_time, 2)} seconds"
#     )

#     print(
#         f"Overall Status : "
#         f"{summary['overall_status']}"
#     )

#     print()
#     print("Results saved:")
#     print(CSV_FILE)
#     print(JSON_FILE)

#     print("=" * 60)


# if __name__ == "__main__":
#     main()

import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

TEST_DURATION_MINUTES = 2

TEST_INTERVAL_SECONDS = 60


CURRENT_FOLDER = os.path.dirname(
    os.path.abspath(__file__)
)


DOCUMENTS_FOLDER = os.path.dirname(
    CURRENT_FOLDER
)


OPTIMIZATION_FOLDER = os.path.join(
    DOCUMENTS_FOLDER,
    "System optimization"
)
OPTIMIZATION_FILE = os.path.join(
    OPTIMIZATION_FOLDER,
    "optimization.py"
)

RESULT_FOLDER = os.path.join(
    CURRENT_FOLDER,
    "milestone_results"
)

os.makedirs(
    RESULT_FOLDER,
    exist_ok=True
)


CSV_FILE = os.path.join(
    RESULT_FOLDER,
    "milestone_metrics.csv"
)

JSON_FILE = os.path.join(
    RESULT_FOLDER,
    "milestone_summary.json"
)

def get_current_time():

    return datetime.now(
        timezone.utc
    ).isoformat()

def check_optimization_file():

    print()
    print("Checking Day 29 application...")
    print(
        "Optimization file:"
    )
    print(
        OPTIMIZATION_FILE
    )

    if not os.path.isfile(
        OPTIMIZATION_FILE
    ):

        print()
        print(
            "ERROR: optimization.py was not found."
        )

        print(
            "Please check the folder:"
        )

        print(
            OPTIMIZATION_FOLDER
        )

        return False

    print(
        "optimization.py found successfully."
    )

    return True


def run_optimization():

    start_time = time.perf_counter()

    try:

        result = subprocess.run(

            [
                sys.executable,
                OPTIMIZATION_FILE
            ],

            capture_output=True,

            text=True,

            timeout=TEST_INTERVAL_SECONDS

        )

        end_time = time.perf_counter()

        processing_time = round(
            end_time - start_time,
            2
        )


        if result.returncode == 0:

            status = "SUCCESS"

        else:

            status = "FAILED"


        output = result.stdout.strip()

        error = result.stderr.strip()

        return {

            "status":
                status,

            "processing_time":
                processing_time,

            "exit_code":
                result.returncode,

            "output":
                output,

            "error":
                error
        }


    except subprocess.TimeoutExpired:

        end_time = time.perf_counter()

        processing_time = round(
            end_time - start_time,
            2
        )

        return {

            "status":
                "TIMEOUT",

            "processing_time":
                processing_time,

            "exit_code":
                -1,

            "output":
                "",

            "error":
                "optimization.py exceeded the test interval."
        }


    except Exception as error:

        return {

            "status":
                "ERROR",

            "processing_time":
                0,

            "exit_code":
                -1,

            "output":
                "",

            "error":
                str(error)
        }


def save_csv(results):

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [

            "cycle",

            "timestamp",

            "status",

            "processing_time_seconds",

            "exit_code"

        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for item in results:

            writer.writerow({

                "cycle":
                    item["cycle"],

                "timestamp":
                    item["timestamp"],

                "status":
                    item["status"],

                "processing_time_seconds":
                    item[
                        "processing_time_seconds"
                    ],

                "exit_code":
                    item["exit_code"]
            })

def save_summary(

    start_time,

    end_time,

    results

):

    total_cycles = len(
        results
    )

    successful_cycles = sum(

        1

        for item in results

        if item["status"] == "SUCCESS"

    )

    failed_cycles = sum(

        1

        for item in results

        if item["status"] != "SUCCESS"

    )

    if total_cycles > 0:

        success_rate = (

            successful_cycles
            / total_cycles

        ) * 100

    else:

        success_rate = 0


    if total_cycles > 0:

        average_processing_time = (

            sum(

                item[
                    "processing_time_seconds"
                ]

                for item in results

            )

            / total_cycles

        )

    else:

        average_processing_time = 0

    if total_cycles > 0 and failed_cycles == 0:

        overall_status = "PASSED"

    elif total_cycles > 0:

        overall_status = (
            "COMPLETED_WITH_ERRORS"
        )

    else:
        overall_status = "FAILED"
    summary = {

        "test_name":
            "Day 30 - Milestone Testing",

        "test_duration_minutes":
            TEST_DURATION_MINUTES,

        "test_interval_seconds":
            TEST_INTERVAL_SECONDS,

        "start_time":
            start_time,

        "end_time":
            end_time,

        "application":
            "optimization.py",

        "total_cycles":
            total_cycles,

        "successful_cycles":
            successful_cycles,

        "failed_cycles":
            failed_cycles,

        "success_rate_percent":
            round(
                success_rate,
                2
            ),

        "average_processing_time_seconds":
            round(
                average_processing_time,
                2
            ),

        "overall_status":
            overall_status
    }

    with open(
        JSON_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )


    return summary

def main():

    print()
    print("=" * 65)

    print(
        "DAY 30 - MILESTONE TESTING"
    )

    print("=" * 65)

    print(
        f"Test Duration : "
        f"{TEST_DURATION_MINUTES} minutes"
    )

    print(
        f"Test Interval : "
        f"{TEST_INTERVAL_SECONDS} seconds"
    )

    print("=" * 65)


    if not check_optimization_file():

        print()
        print(
            "Milestone test cannot start."
        )

        sys.exit(1)


    print()
    print(
        "Day 29 application is ready."
    )


    start_time = get_current_time()

    test_start = time.time()

    results = []

    cycle = 0


    try:

        while (

            time.time() - test_start

        ) < (

            TEST_DURATION_MINUTES * 60

        ):

            cycle += 1

            print()
            print(
                "-" * 65
            )

            print(
                f"Running test cycle {cycle}..."
            )

            result = run_optimization()

            record = {

                "cycle":
                    cycle,

                "timestamp":
                    get_current_time(),

                "status":
                    result["status"],

                "processing_time_seconds":
                    result[
                        "processing_time"
                    ],

                "exit_code":
                    result["exit_code"]
            }


            results.append(
                record
            )

            print(
                f"Status     : "
                f"{result['status']}"
            )

            print(
                f"Processing : "
                f"{result['processing_time']} "
                f"seconds"
            )

            print(
                f"Exit code  : "
                f"{result['exit_code']}"
            )


            if result["error"]:

                print(
                    "Error:"
                )

                print(
                    result["error"]
                )


            save_csv(
                results
            )


            elapsed = (
                time.time()
                - test_start
            )

            remaining = (
                TEST_DURATION_MINUTES * 60
                - elapsed
            )


            if remaining <= 0:

                break


            wait_time = min(

                TEST_INTERVAL_SECONDS,

                remaining

            )
            print()
            print(
                f"Waiting {int(wait_time)} "
                f"seconds before next cycle..."
            )

            time.sleep(
                wait_time
            )

    except KeyboardInterrupt:

        print()
        print(
            "Test stopped manually."
        )

    end_time = get_current_time()


    summary = save_summary(

        start_time,

        end_time,

        results

    )


    print()
    print("=" * 65)

    print(
        "MILESTONE TEST COMPLETED"
    )

    print("=" * 65)

    print(
        f"Total Cycles  : "
        f"{summary['total_cycles']}"
    )

    print(
        f"Successful    : "
        f"{summary['successful_cycles']}"
    )

    print(
        f"Failed        : "
        f"{summary['failed_cycles']}"
    )

    print(
        f"Success Rate  : "
        f"{summary['success_rate_percent']}%"
    )

    print(
        f"Average Time  : "
        f"{summary['average_processing_time_seconds']} "
        f"seconds"
    )

    print(
        f"Overall Status: "
        f"{summary['overall_status']}"
    )
    
    print()
    print(
        "Results saved:"
    )

    print(
        CSV_FILE
    )

    print(
        JSON_FILE
    )

    print("=" * 65)


if __name__ == "__main__":

    main()