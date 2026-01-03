class LeaveRequestStatus:
    """Статусы запроса на временное отсутствие"""

    ON_APPROVAL = 'on_approval'
    REJECTED = 'rejected'
    PLANNED = 'planned'
    COMPLETED = 'completed'
    STATUSES = {
        ON_APPROVAL: 'На согласовании',
        REJECTED: 'Отказано',
        PLANNED: 'Запланировано',
        COMPLETED: 'Выполнено',
    }
