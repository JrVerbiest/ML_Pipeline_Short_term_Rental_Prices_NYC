#!/usr/bin/env python
"""
 Download from W&B the raw dataset and apply some basic data cleaning,
 export the result to a new artifact
"""
import argparse
import logging

from numpy.core.fromnumeric import argsort
import wandb
import os
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    logger.info("download artifact: %s", args.input_artifact)
    df = pd.read_csv(artifact_local_path)

    logger.info("remove outliers (min-max): %i - %i", args.min_price, args.max_price)
    min_price = args.min_price
    max_price = args.max_price
    idx = df["price"].between(min_price, max_price)
    df = df[idx].copy()

    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()

    tmp_dir = os.path.join(args.tmp_dir,args.output_artifact)
    logger.info("save clean artifact, path: %s", tmp_dir)
    df.to_csv(tmp_dir, index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description
    )

    artifact.add_file(tmp_dir)
    run.log_artifact(artifact)

    artifact.wait()
    logger.info("artifact uploaded")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This steps cleans the data")

    parser.add_argument(
        "--tmp_dir",
        type=str,
        help="temporary directory",
        required=True
    )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="input artifact name (*.csv)",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="output artifact name (*.csv)",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="output artifact type",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="output artifact description",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="the minimum price - outlier left (min.) boundary",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="the maximum price - outlier right (max.) boundary",
        required=True
    )


    args = parser.parse_args()

    go(args)