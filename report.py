"""This module is creation --Report of Monaco 2018 Racing F1--"""
import os, click
from datetime import datetime, timedelta
from pydantic import BaseModel, Field, validator, root_validator, ValidationError
from tabulate import tabulate

ABBREVIATION_TXT = "abbreviations.txt"
START_LOG = "start.log"
END_LOG = "end.log"
BASE_DIR = os.path.dirname(__file__)
_full_path = os.path.join(BASE_DIR, '../data')
SEPARATOR_FOR_REPORT = 18  # For this type of tabulate = 15 drivers + 3 headers


class Abbreviation(BaseModel):
    """Class for abbreviation decryption data from abbreviations.txt"""
    driver_id: str
    name: str
    team: str


class EndLap(BaseModel):
    """Class for storing data from end.log"""
    driver_id: str
    end_lap: datetime


class StartLap(BaseModel):
    """Class for storing data from start.log"""
    driver_id: str
    start_lap: datetime


class Driver(BaseModel):
    """Consolidated class and validate for information about drivers and F1 race Monaco"""
    driver_id: str = Field(..., pattern=r'^[A-Z]{3}$')
    name: str = Field(..., pattern=r'^\w+\s\w+$')
    team: str = Field(..., pattern=r'^[A-Z ]+$')
    start_lap: datetime
    end_lap: datetime
    best_lap: timedelta = None

    @root_validator(pre=True)
    def calculate_best_lap(cls, values):
        """Function to create and validate the best lap parameter"""
        start_lap = values.get('start_lap')
        end_lap = values.get('end_lap')

        if start_lap and end_lap:
            best_lap = end_lap - start_lap
            if best_lap.total_seconds() < 0:
                values['start_lap'], values['end_lap'] = end_lap, start_lap
                print("--Attention! Time End lap is less than Start lap time!--")

        values['best_lap'] = values['end_lap'] - values['start_lap']
        return values


def get_abbreviations(path: str) -> list[Abbreviation]:
    """Function reads the file abbreviations.txt and creates a container to store class Abbreviation instances"""
    abbreviations = []  # container list of class Abbreviation

    with open(os.path.join(path, ABBREVIATION_TXT), encoding='utf-8') as file:
        for line in file:
            if line.strip():
                driver_id, name, team = line.strip().split('_')

                data = {'driver_id': driver_id, 'name': name, 'team': team}
                abbreviation = Abbreviation(**data)
                abbreviations.append(abbreviation)
    return abbreviations


def get_end(path: str) -> list[EndLap]:
    """Function reads the file end.log and creates a container to store class EndLap instances"""
    endlaps = []  # container list of class EndLap

    with open(os.path.join(path, END_LOG), encoding='utf-8') as file:
        for line in file:
            if line.strip():
                driver_id = line.strip()[:3]
                end_lap = line.strip()[3:]

                data = {'driver_id': driver_id, 'end_lap': end_lap}
                endlap = EndLap(**data)
                endlaps.append(endlap)
    return endlaps


def get_start(path: str) -> list[StartLap]:
    """Function reads the file start.log and creates a container to store class StartLap instances"""
    startlaps = []  # container list of class StartLap

    with open(os.path.join(path, START_LOG), encoding='utf-8') as file:
        for line in file:
            if line.strip():
                driver_id = line.strip()[:3]
                start_lap = line.strip()[3:]

                data = {'driver_id': driver_id, 'start_lap': start_lap}
                startlap = StartLap(**data)
                startlaps.append(startlap)
    return startlaps


def get_drivers(path: str = _full_path) -> list[Driver]:
    """Function to create a class Driver from 3 containers of class instances: Abbreviation, StartLap, EndLap;
    comparing data by driver_id. Also creates a class Driver instance container - list _drivers_"""
    drivers_all = []  # container list of class Driver

    for abbreviation in get_abbreviations(path):
        for endlap in get_end(path):
            for startlap in get_start(path):
                if abbreviation.driver_id == endlap.driver_id == startlap.driver_id:
                    driver = Driver(
                        driver_id=abbreviation.driver_id,
                        name=abbreviation.name,
                        team=abbreviation.team,
                        end_lap=endlap.end_lap,
                        start_lap=startlap.start_lap)
                    drivers_all.append(driver)
    # print(drivers_all[1])
    return drivers_all


@click.command()
@click.option('--file', type=click.Path(exists=True), required=True, help='Specify the path to the source files.')
@click.option('--asc', is_flag=True, help='Get the F1 Monaco report in ascending lap time.')
@click.option('--desc', is_flag=True, help='Get the F1 Monaco report by descending lap times.')
@click.option('--driver', help='Get the F1 Monaco report for a specific rider')
def main_cli(file: str, asc: bool, desc: bool, driver: str) -> None:
    """This application will create and report the results of the F1 Monaco 2018 race from the
    input race log files, the path to which you specify in the --file command. There are several
    options for getting the report."""
    if not file:
        raise click.UsageError("---Option --file is required!!!---")

    if (asc and desc) or (asc and driver) or (driver and desc):
        raise click.UsageError("--Options --asc,--desc,--driver cannot be used together!--")
    elif driver:
        driver_report(driver, file)  # Call a function to get the report for a specific driver.
    else:
        if not asc and not desc:
            asc = True  # Default to ascending order if neither --asc nor --desc is provided.
        build_report(asc, file)  # Call a function to get the overall report.


def driver_report(one: str, path: str = _full_path) -> None:
    """Building report on the Monaco race for a specific driver."""
    sorted_drivers = sorted(get_drivers(path), key=lambda x: x.best_lap)  # report по возрастанию времени круга

    table = []
    for i, driver in enumerate(sorted_drivers, start=1):  # создаем список для отчета
        table.append([i, driver.name, driver.team, format_timedelta(driver.best_lap)])

    one_driver = [e for e in table if e[1] == one.strip()]  # вынимаем из списка конкретного гонщика
    if not one_driver:
        raise click.UsageError("--Enter the correct driver name!--")

    headers = ["№", "NAME DRIVER", "TEAM FORMULA 1", "BEST LAP"]

    # Вывод результата в виде таблицы
    print("  ---------  Report of Monaco 2018 Racing F1  ---------")
    print(tabulate(one_driver, headers, tablefmt="rounded_outline"))


def build_report(asc: bool = True, path: str = _full_path) -> None:
    """Building an overall report on the Monaco race."""
    if asc:
        sorted_drivers = sorted(get_drivers(path), key=lambda x: x.best_lap)  # report по возрастанию времени круга
    else:
        sorted_drivers = sorted(get_drivers(path), key=lambda x: -x.best_lap)  # report по убыванию времени круга

    table = []
    for i, driver in enumerate(sorted_drivers, start=1):  # создаем список для отчета
        table.append([i, driver.name, driver.team, format_timedelta(driver.best_lap)])

    headers = ["№", "NAME DRIVER", "TEAM FORMULA 1", "BEST LAP"]
    table_sep = tabulate(table, headers, tablefmt="rounded_outline")

    rows = table_sep.split("\n")  # Вставляем строку-разделитель
    rows.insert(SEPARATOR_FOR_REPORT, "-" * len(rows[0]))  # Вставляем строку-разделитель после 15гонщика
    table_with_separator = "\n".join(rows)  # Вставляем строку-разделитель

    # Вывод результатов в виде таблицы
    print("      ---------  Report of Monaco 2018 Racing F1  ---------")
    print(table_with_separator)


def format_timedelta(time_obj: timedelta) -> str:
    """Function format the lap time from the format -timedelta-"""
    return f"{time_obj.seconds // 60}:{time_obj.seconds % 60:02d}:{str(time_obj.microseconds)[:3]}"


if __name__ == '__main__':
    # main_cli()
    # build_report()
    driver_report('Kimi Räikkönen')
    # build_report(False)
    # prob = (driver.model_dump() for driver in get_drivers())
    # print(tabulate(prob, tablefmt="psql", showindex=range(1, len(get_drivers()) + 1)))

    
    # def build_report(start_times: dict, end_times: dict, drivers_dict: dict, desc=False):
    #     drivers = []
    #     for driver_id, driver_data in drivers_dict.items():
    #         lap_time = get_lap_time(start_times[driver_id], end_times[driver_id])
    #         drivers.append(Driver(driver_id=driver_id, name=driver_data[0], team=driver_data[1], lap_time=lap_time))
