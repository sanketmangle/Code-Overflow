import matplotlib.pyplot as plt
import numpy as np
from math import exp

# Função para o potencial de membrana
def AdEx(V, Vr, delta_t, Vth, R, u, Iapp, tau_m):

    membrane_potential = -(V - Vr) + delta_t * \
        np.exp((V - Vth)/delta_t) - (R * u) + (R * Iapp)
    membrane_potential = membrane_potential/tau_m

    return membrane_potential


def adaptation(V, Vr, u, a, tau_u):

    du = (a * (V - Vr)) - u
    du = du/tau_u

    return du


def simulation(time_sumlation, start_Iapp, end_Iapp, V0, u0, Vr, dt, Iapp, Vth, tau_m, Vreset, R, delta_t, a, b, tau_u, Vpico, type_neuron):
    time = np.arange(0, time_simulation, dt)
    V = np.zeros(len(time))
    V[0] = V0
    u = np.zeros(len(time))
    u[0] = u0
    spikes = np.zeros(len(time))
    Iapp_simulation = np.zeros(len(time))

    for i in range(1, len(time)):
        if (i >= start_Iapp and i <= end_Iapp):
            Iapp_simulation[i] = Iapp
        else:
            Iapp_simulation[i] = 0

        V[i] = V[i - 1] + (dt * AdEx(V=V[i - 1], Vr=Vr, delta_t=delta_t,
                                     Vth=Vth, R=R, u=u[i - 1], Iapp=Iapp_simulation[i], tau_m=tau_m))
        u[i] = u[i - 1] + (dt * adaptation(V=V[i - 1], Vr=Vr,
                                           u=u[i - 1], a=a, tau_u=tau_u))

        if (V[i] >= Vpico):
            V[i] = Vreset
            u[i] = u[i] + b
            spikes[i] = 1

    fig, axs = plt.subplots(3, figsize=(20, 8))
    fig.suptitle(
        f'Modelo AdEx com corrente adaptativa modelo -> {type_neuron}')
    axs[0].plot(time, Iapp_simulation, c='red')
    axs[0].set(ylabel='Iapp (nA)')
    axs[1].plot(time, V)
    axs[1].set(ylabel="V (mV)")
    axs[2].plot(time, u, c='g')
    axs[2].set(ylabel='Isra (nA)')
    axs[2].set(xlabel='Time (s)')
    plt.savefig(f'exe3{type_neuron}.png', format='png')
    plt.show()


# Parametros
dt = 0.1
Vr = -70
Vth = -50
R = 0.500
delta_t = 2
Vpico = 20
Iapp = 65
time_simulation = 1500  # 1,5 s


simulation(time_sumlation=time_simulation, start_Iapp=5000, end_Iapp=10000, V0=Vr, u0=0, Vr=Vr, dt=dt,
           Iapp=Iapp, Vth=Vth, tau_m=9.9, Vreset=-46, R=R, delta_t=delta_t, a=0.5, b=7, tau_u=100, Vpico=Vpico, type_neuron="(Irregular)")

simulation(time_sumlation=time_simulation, start_Iapp=5000, end_Iapp=10000, V0=Vr, u0=0, Vr=Vr, dt=dt,
           Iapp=Iapp, Vth=Vth, tau_m=20, Vreset=-55, R=R, delta_t=delta_t, a=0, b=5, tau_u=100, Vpico=Vpico, type_neuron="(Com adaptação)")

simulation(time_sumlation=time_simulation, start_Iapp=5000, end_Iapp=10000, V0=Vr, u0=0, Vr=Vr, dt=dt,
           Iapp=Iapp, Vth=Vth, tau_m=5, Vreset=-46, R=R, delta_t=delta_t, a=-0.5, b=7, tau_u=100, Vpico=Vpico, type_neuron="(Rajadas)")
