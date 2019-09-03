def calculate_nmf(folder, trace_file, loco_file, fps=7.51, lower_thresh = -0.2, upper_thresh = 0.5, n_components=3):
    ''' Calculates the non-negative matrix factorization for a dataset that is in folder

    Keyword arguments:
    folder - folder path containing locomotion and data file
    trace_file - path to data matrix, relative to folder
    loco_file - path to locomotion data, relative to folder
    fps - frames per second of locomotion recording (default = 7.51)
    lower_thresh - Lower speed cutoff (default = -0.2)
    upper_thresh - Upper speed cutoff (default = 0.5)
    n_components - The number of components to calculate in the non-negative matrix factorization (default = 3)

    Output arguments
    W - The weight of each cell in the different components from the NMF
    H - The time series for each components from the NMF
    '''
    cell_fluorescence = scipy.io.loadmat(os.path.join(folder,trace_file))['traces']
    cell_fluorescence[cell_fluorescence<0] = 0
    locomotion = scipy.io.loadmat(os.path.join(folder,'locomotion.mat'))['loco']

    velocity = np.diff(locomotion, axis=0)
    velocity = np.insert(velocity, 0, 0)
    velocity[velocity<lower_thresh/fps] = 0
    velocity[velocity>upper_thresh/fps] = 0

    model = NMF(n_components=3, init='random', random_state=0)
    W = model.fit_transform(cell_fluorescence)
    H = model.components_

    for i,h in enumerate(H):
        plt.figure()
        plt.plot(h.T,)
        plt.xlabel('Frames')
        plt.ylabel(f'Component {i} weight')
        plt.show()

    return W, H
