# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:02:27 2016

@author: James Rocker
"""

import imp, pip, time

package = "numpy"


def install_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print("Error " + package + " library is missing ")
        var = input(
            "Do you want to download and install the "
            + package
            + " library? (Note, this download and install might take a while) "
        )
        if var in ["no", "n", "No", "N", "NO"]:
            print(
                "Error, "
                + package
                + " not installed, please install the library before attempting to run this program."
            )
            time.sleep(5)
            quit()
        else:
            pip.main(["install", package])


install_func(package)

package = "matplotlib"
install_func(package)

import matplotlib.pyplot as plt
import numpy as np

data_a = [[1, 2, 5], [5, 7, 1, 2, 5], [7, 2, 5]]
data_b = [[6, 4, 2], [1, 2, 5, 3, 2], [2, 3, 5, 1]]
xticks = ["10m", "50m", "100m"]


def set_box_color(bp, color):
    plt.setp(bp["boxes"], color=color)
    plt.setp(bp["whiskers"], color=color)
    plt.setp(bp["caps"], color=color)
    plt.setp(bp["medians"], color=color)


plt.figure()


def create_graph():
    bpl = plt.boxplot(
        data_a, positions=np.array(range(len(data_a))) * 2.0 - 0.4, sym="", widths=0.6
    )
    bpr = plt.boxplot(
        data_b, positions=np.array(range(len(data_b))) * 2.0 + 0.4, sym="", widths=0.6
    )
    set_box_color(bpl, "#D7191C")
    set_box_color(bpr, "#2C7BB6")

    # draw temporary red and blue lines and use them to create a legend
    plt.plot([], c="#D7191C", label="Sample data 1")
    plt.plot([], c="#2C7BB6", label="Sample data 2")
    plt.legend()

    plt.xticks(range(0, len(xticks) * 2, 2), xticks)
    plt.xlim(-2, len(xticks) * 2.2)
    plt.xlabel("Sample Category")
    plt.ylim(0, 10)
    plt.ylabel("Sample Scores")
    plt.tight_layout()
    plt.savefig("boxcompare.png")


create_graph()
