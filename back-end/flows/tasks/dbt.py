def seed_dbt():
    """A task to seed dbt."""
    from prefect.tasks.dbt import DbtShellTask
    from utility.common import load_dot_env

    load_dot_env()

    dbt_task = DbtShellTask(
        profile_name="default",
        environment="dev",
        helper_script="cd dbt",
        profiles_dir=".",
    )(command="dbt seed")

    return dbt_task


def run_dbt():
    """A task to run dbt."""
    from prefect.tasks.dbt import DbtShellTask
    from utility.common import load_dot_env

    load_dot_env()

    dbt_task = DbtShellTask(
        profile_name="default",
        environment="dev",
        helper_script="cd dbt",
        profiles_dir=".",
    )(command="dbt run")

    return dbt_task


def doc_dbt():
    """A task to generate dbt documentation."""
    from prefect.tasks.dbt import DbtShellTask
    from utility.common import load_dot_env

    load_dot_env()

    dbt_task = DbtShellTask(
        profile_name="default",
        environment="dev",
        helper_script="cd dbt",
        profiles_dir=".",
    )(command="dbt docs generate")

    return dbt_task
