{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPYNm5F+r0RVSTRRocFaAMv"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0fLX3GElSB7r"
      },
      "outputs": [],
      "source": [
        "@dataclass(frozen=True)\n",
        "class CastSpec:\n",
        "  cast_time: float = 0\n",
        "  recast_time: float = 1\n",
        "  is_GCD: bool = True\n",
        "  animation_lock: float = 0.65\n",
        "  cast_time_ignores_haste: bool = False\n",
        "  recast_time_ignores_haste: bool = False"
      ]
    }
  ]
}