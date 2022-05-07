from click import prompt

from ...codebase.providers import get_provider
from ...config import DEFAULT_PROVIDER
from .searcher import get_searcher
from time import sleep

from .prompts import get_prompt_manager


def prompt_user(logger, anime_list_genexp, provider):

    manager = get_prompt_manager()

    return manager(
        logger,
        anime_list_genexp,
        processor=lambda component: (component, provider),
        component_name="search result",
        fallback=({}, None),
        error_message=f"Failed to find anything of that query on {provider!r}. Try searching on other providers.",
        stdout_processor=lambda component: f"{component[0]['name']} / {component[0]['anime_url']}",
    )


def process_query(
    session, query: str, logger, *, provider=DEFAULT_PROVIDER, auto=False, auto_index=1
):

    _, module, provider_name = get_provider(query, raise_on_failure=False)

    if module:
        return {"anime_url": query}, provider_name

    *provider_name, custom_query = query.split(":", 1)

    searcher = get_searcher(":".join(provider_name))

    if not searcher:
        searcher, custom_query = get_searcher(provider), query

    genexp = searcher(session, custom_query)

    # if genexp has no results remove some words from search and retry
    list = [*genexp]
    retries = 0
    while len(list) == 0 and retries < 2:
        sleep(2)
        lenght = len(custom_query.split(" "))
        if lenght < 2:
            break
        custom_query = ' '.join(custom_query.split(' ')[:round(lenght/2)])
        genexp = searcher(session, custom_query)
        list = [*genexp]
        retries += 1

    # convert list to generator
    genexp = iter(list)

    if not auto:
        return prompt_user(logger, genexp, searcher.provider)
    return list(genexp)[auto_index - 1], searcher.provider
