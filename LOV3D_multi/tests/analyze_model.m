function [k2] = analyze_model(model_setup, forcing_setup, numerics_setup)

    % Generate numerics and preliminary model
    [numerics, prelim_model] = set_boundary_indices(...
        numerics_setup, model_setup...
    );

    % Reformat interior model for compatibility
    [model] = get_rheology(prelim_model, numerics, forcing_setup);

    % Get Love number spectra and radial functions
    [love_spectra, ~] = get_Love(...
        model, forcing_setup, numerics...
    );

    k2 = love_spectra.k;

end