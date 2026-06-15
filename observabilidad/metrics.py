import time
import logging


logging.basicConfig(level=logging.INFO)


def log_request_metrics(
    question: str,
    response_time: float,
    token_usage: int
):
    logging.info(
        f"""
        Question: {question}
        Response Time: {response_time} seconds
        Token Usage: {token_usage}
        """
    )


def measure_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        logging.info(
            f"{func.__name__} executed in {end - start:.2f} seconds"
        )

        return result

    return wrapper
