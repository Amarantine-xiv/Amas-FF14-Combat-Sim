{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNnsNxdhRG+vcqG0BBdmdwa"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "@dataclass(frozen=True)\n",
        "class CastSpec:\n",
        "  cast_time: float = 0\n",
        "  recast_time: float = 1\n",
        "  is_GCD: bool = True\n",
        "  animation_lock: float = 0.65\n",
        "  cast_time_ignores_haste: bool = False\n",
        "  recast_time_ignores_haste: bool = False"
      ],
      "metadata": {
        "id": "hoRLkIcvUOG7"
      }
    }
  ]
}