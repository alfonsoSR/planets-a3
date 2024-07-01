HOME = pwd;

layer = 3;
property = "mu0";

label = "Layer " + num2str(layer) + " " + property;

data = load(HOME + "/output/layer" + num2str(layer) + "_" + property + ".txt");

figure;
subplot(1, 2, 1);
hold on
plot(data(1, :), data(2, :));
xlabel(label);
ylabel("Real k2");
hold off

subplot(1, 2, 2);
hold on
plot(data(1, :), data(3, :));
xlabel(label);
ylabel("Imag k2");
hold off