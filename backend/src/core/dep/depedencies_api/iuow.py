from typing import Type
from abc import abstractmethod, ABC
from src.databases.postgres.repositories import (
    UserRepository,
    UserTypesRepository,
    CoursesRepository,
    HobbyCoursesRepository,
    HobbiesRepository,
    VacanciesRepository,
    UniversityRepository,
    PortfolioRepository,
    UserHobbiesRepository,
    RecommendsRepository,
)  # noqa


class InterfaceUnitOfWork(ABC):

    user_repository: Type[UserRepository]
    user_type_repository: Type[UserTypesRepository]
    courses_repository: Type[CoursesRepository]
    hobby_courses_repository: Type[HobbyCoursesRepository]
    hobbies_repository: Type[HobbiesRepository]
    vacancies_repository: Type[VacanciesRepository]
    university_repository: Type[UniversityRepository]
    portfolio_repository: Type[PortfolioRepository]
    user_hobbies_repository: Type[UserHobbiesRepository]
    recommends_repository: Type[RecommendsRepository]

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError
