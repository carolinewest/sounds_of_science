import matplotlib.pyplot as plt
import os
'''
Takes a MIDI DataFrame and an optional GC profile, and generates various plots.
the plots include:
1. Distribution of notes
2. Velocity over time
3. Distribution of note durations
4. Instrument usage
5. Channel usage
6. Pitch over time
7. GC content profile (if provided)
Outputs the plots to the specified directory.

'''

def plot_music_data(df, gc_profile=None, output_dir='example_file_and_output'):
    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # 1. Note distribution
    plt.figure()
    df['Note'].value_counts().sort_index().plot(kind='bar')
    plt.xlabel('MIDI Note')
    plt.ylabel('Count')
    plt.title('Distribution of Notes')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'note_distribution.png'))
    plt.close()

    # 2. Velocity over time
    plt.figure()
    plt.plot(df['Time'], df['Velocity'])
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity (GC Content) Over Time')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'velocity_over_time.png'))
    plt.close()

    # 3. Duration distribution
    plt.figure()
    df['Duration'].value_counts().sort_index().plot(kind='bar')
    plt.xlabel('Duration')
    plt.ylabel('Count')
    plt.title('Distribution of Note Durations')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'duration_distribution.png'))
    plt.close()

    # 4a. Instrument usage
    plt.figure()
    df['Instrument'].value_counts().plot(kind='bar')
    plt.xlabel('Instrument')
    plt.ylabel('Count')
    plt.title('Instrument Usage')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'instrument_usage.png'))
    plt.close()

    # 4b. Channel usage
    plt.figure()
    df['Channel'].value_counts().plot(kind='bar')
    plt.xlabel('Channel')
    plt.ylabel('Count')
    plt.title('Channel Usage')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'channel_usage.png'))
    plt.close()

    # 5. Pitch over time
    plt.figure()
    plt.plot(df['Time'], df['Note'])
    plt.xlabel('Time')
    plt.ylabel('Note (Pitch)')
    plt.title('Pitch Over Time')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pitch_over_time.png'))
    plt.close()

    # 6. GC content profile (optional)
    if gc_profile is not None:
        plt.figure()
        plt.plot(gc_profile)
        plt.xlabel('Window Index')
        plt.ylabel('GC Content')
        plt.title('GC Content Profile')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'gc_content_profile.png'))
        plt.close()
