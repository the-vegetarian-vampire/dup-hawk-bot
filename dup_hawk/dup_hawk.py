import os
from typing import List

import click
import openai
from dotenv import load_dotenv
from openai import Embedding
from openai.embeddings_utils import get_embedding
from scipy import spatial

from pygithub import Github

from .__version__ import __title__, __version__

load_dotenv()

EMBEDDING_MODEL = "text-embedding-ada-002"
SIMILARITY_THRESHOLD = 0.85


@click.command()
@click.version_option(
    version=__version__,
    prog_name=__title__,
)
@click.option(
    "--git-repo-url",
    default=None,
    help="GitHub repo URL that you want to mark duplicate issues for.",
)
@click.option(
    "--git-pat-token",
    default=os.getenv("GITHUB_PAT_TOKEN"),
    help="GitHub repo URL that you want to mark duplicate issues for.",
)
def mark_duplicates_click(git_repo_url: str, git_pat_token: str):
    mark_duplicates(git_repo_url, git_pat_token)


def mark_duplicates(git_repo_url: str, git_pat_token: str):
    openai.key = os.getenv("OPENAI_API_KEY")
    g: Github = Github(git_pat_token)
    repo_issues: List[dict] = g.get_issues(git_repo_url, state="open")

    # Make this a dict
    titles_and_id = [
        {key: dic[key] for key in ("id", "title")}
        for dic in repo_issues
        if dic.get("title") is not "update"
    ]
    bodies_and_id = [
        {key: dic[key] for key in ("id", "title")}
        for dic in repo_issues
        if dic.get("body") is not None
    ]

    titles_embeddings = Embedding.create(
        input=titles_and_id.values(), model=EMBEDDING_MODEL
    )
    bodies_embeddings = Embedding.create(
        input=bodies_and_id.values(), model=EMBEDDING_MODEL
    )
    duplicates = find_duplicates(titles_and_id, titles_embeddings, SIMILARITY_THRESHOLD)
    breakpoint()


def find_duplicates(
    titles: List[dict], embeddings: List[Embedding], similarity_threshold: float
):
    """
    Find duplciates based on the titles

    Args:
        titles (List[str]): _description_
        embeddings (List[Embedding]): _description_
        similarity_threshold (float): A float between 0 and 1

    Returns:
        _type_: _description_
    """

    duplicates = []

    for index in range(len(embeddings)):
        for index_j in range(index + 1, len(embeddings)):
            similarity = 1 - spatial.distance.cosine(
                embeddings.data[index]["embedding"],
                embeddings.data[index_j]["embedding"],
            )
            if similarity > similarity_threshold:
                duplicates.append((titles[index], titles[index_j], similarity))

    return duplicates


def compare_issues(issue1, issue2):
    pass


# def get_owner_and_repo(url: str) -> tuple[str, str]:
#     parsed_url = urlparse(url)
#     path = parsed_url.path
#     owner, repo = path.strip("/").split("/")[0:2]
#     return owner, repo


# def mark_issue_as_duplicate(issue):
#     pass


# def get_issues_from_repo():
#     pass


if __name__ == "__main__":
    mark_duplicates_click()
