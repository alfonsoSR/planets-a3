from pathlib import Path
import numpy as np
from nastro import graphics as ng

sourcedir = Path(__file__).parents[1] / "LOV3D_multi/output"


if __name__ == "__main__":

    # Load all the data

    layers = [1, 2, 3, 4]
    properties = [
        ["R0", "rho0"],
        ["R0", "rho0", "eta0", "mu0"],
        ["R0", "rho0", "eta0", "mu0"],
        ["rho0", "eta0", "mu0"],
    ]
    names = ["Core", "Mantle", "Asthenosphere", "Crust"]
    nominal_k2 = [0.61183, -0.015009]

    layers_dict = {layer: prop for layer, prop in zip(layers, properties)}

    data = {}
    for layer in layers:
        current_layer = {}
        for property in properties[layer - 1]:
            info = np.loadtxt(sourcedir / f"layer{layer}_{property}.txt")
            current_layer[property] = info
        data[layer] = current_layer

    for layer, name in zip(layers, names):
        for property in properties[layer - 1]:
            print(name, property, data[layer][property][0])

    subplot_setup = ng.PlotSetup(xscale="log")
    mosaic_setup = ng.PlotSetup(
        canvas_size=(7, 9),
        save=True,
        show=False,
        dir="media",
        name="k2-interior-properties.png",
    )

    with ng.Mosaic("ab;cd;ef;gh", mosaic_setup) as mosaic:

        # Radius
        radius_setup = ng.PlotSetup(
            xlabel="Radius [x10$^3$ km]",
            ylabel="Real $k_2$",
            legend=True,
        )
        with mosaic.subplot(radius_setup) as ax:
            for layer, name in zip(layers, names):
                if "R0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf, label=name, fmt="-o")
                    continue
                ax.line(
                    data[layer]["R0"][0] * 1e-3,
                    data[layer]["R0"][1],
                    label=name,
                    fmt="-o",
                )

        radius_setup = ng.PlotSetup(
            xlabel="Radius [x10$^3$ km]",
            ylabel="Imaginary $k_2$ [x10$^{-2}$]",
            legend=False,
        )
        with mosaic.subplot(radius_setup) as ax:
            for layer, name in zip(layers, names):
                if "R0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf)
                    continue
                ax.line(
                    data[layer]["R0"][0] * 1e-3,
                    data[layer]["R0"][2] * 1e2,
                    label=name,
                    fmt="-o",
                )

        # Density
        rho_setup = ng.PlotSetup(
            xlabel="Density [x10$^3$ kg/m$^3$]",
            ylabel="Real $k_2$",
            legend=False,
        )
        with mosaic.subplot(rho_setup) as ax:
            for layer, name in zip(layers, names):
                ax.line(
                    data[layer]["rho0"][0] * 1e-3,
                    data[layer]["rho0"][1],
                    label=name,
                    fmt="-o",
                )

        rho_setup = ng.PlotSetup(
            xlabel="Density [x10$^3$ kg/m$^3$]",
            ylabel=r"Imaginary $k_2$ [x10$^{-2}$]",
            legend=False,
        )
        with mosaic.subplot(rho_setup) as ax:
            for layer, name in zip(layers, names):
                ax.line(
                    data[layer]["rho0"][0] * 1e-3,
                    data[layer]["rho0"][2] * 100,
                    label=name,
                    fmt="-o",
                )

        # Viscosity
        eta_setup = ng.PlotSetup(
            xlabel="Viscosity [Pa s]",
            ylabel="Real $k_2$",
            legend=False,
            xscale="log",
        )
        with mosaic.subplot(eta_setup) as ax:
            for layer, name in zip(layers, names):
                if "eta0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf)
                    continue
                ax.line(
                    data[layer]["eta0"][0],
                    data[layer]["eta0"][1],
                    label=name,
                    fmt="-o",
                )

        eta_setup = ng.PlotSetup(
            xlabel="Viscosity [Pa s]",
            ylabel="Imaginary $k_2$",
            legend=False,
            xscale="log",
        )
        with mosaic.subplot(eta_setup) as ax:
            for layer, name in zip(layers, names):
                if "eta0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf)
                    continue

                ax.line(
                    data[layer]["eta0"][0],
                    data[layer]["eta0"][2],
                    label=name,
                    fmt="-o",
                )

        # Shear modulus
        shear_setup = ng.PlotSetup(
            xlabel="Shear modulus [Pa]",
            ylabel="Real $k_2$",
            legend=False,
            xscale="log",
        )
        with mosaic.subplot(shear_setup) as ax:
            for layer, name in zip(layers, names):
                if "mu0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf)
                    continue
                ax.line(
                    data[layer]["mu0"][0],
                    data[layer]["mu0"][1],
                    label=name,
                    fmt="-o",
                )

        eta_setup = ng.PlotSetup(
            xlabel="Shear modulus [Pa]",
            ylabel="Imaginary $k_2$",
            legend=False,
            xscale="log",
        )
        with mosaic.subplot(eta_setup) as ax:
            for layer, name in zip(layers, names):
                if "mu0" not in layers_dict[layer]:
                    ax.line(np.inf, np.inf)
                    continue

                ax.line(
                    data[layer]["mu0"][0],
                    data[layer]["mu0"][2],
                    label=name,
                    fmt="-o",
                )
        # for layer in range(1, 5):
        #     try:
        #         data = np.loadtxt(outdir / f"layer{layer}_{property}.txt")
        #         left.line(data[0], data[1], label=f"layer {layer}", fmt="-o")
        #         right.line(data[0], data[2], label=f"layer {layer}", fmt="-o")
        #     except FileNotFoundError:
        #         pass

        # left.__exit__(None, None, None)
        # right.__exit__(None, None, None)
