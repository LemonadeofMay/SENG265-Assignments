/** @file song_analyzer.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process song
 *  data and printing it in a different format.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Angadh S.
 *  @author Juan G.
 *  @author Hyesung T.
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * @brief The maximum line length.
 *
 */
#define MAX_LINE_LEN 132
#define BEFORE ("before_2020s.csv")
#define DURING ("during_2020s.csv")
#define OUTPUTFILE ("output.csv")
#define TITLE 0
#define ARTIST 1
#define YEAR 3
#define PLAYLIST 4
#define KEY 6
#define SCALE 7
#define FIELDS 8


/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */

// Prototypes
FILE* openFile (char*);
FILE* createFile(void);
void writeOutput (FILE*, char*, char*);
int stringLoop(char*, char*);
void question1 (void);
void question2 (void);
void question3 (void);
void question4 (void);
void question5 (void);

int main(int argc, char *argv[])
{
    // TODO: your code.
    char* question = argv[1];
    char* inputfile = argv[2];

    if (strcmp(question, "--question=1") == 0) {
        question1();
    } else if (strcmp(question, "--question=2") == 0) {
        question2();
    } else if (strcmp(question, "--question=3") == 0) {
        question3();
    } else if (strcmp(question, "--question=4") == 0) {
        question4();
    } else if (strcmp(question, "--question=5") == 0) {
        question5();
    } else {
        printf("Cannot answer this question");
        exit(EXIT_FAILURE);
    }
    exit(0);
}

/**
 * Function: openFile
 * --------------
 * @brief Opens the file to read
 *
 * @param filename The name of the csv file to be opened
 * @return FILE* The opened file
 *
 */
FILE* openFile (char* filename) {
    FILE* ifp = fopen(filename, "r");
    if (ifp == NULL) {
        printf("File open error");
        exit(EXIT_FAILURE);
    }
    return(ifp);
}

/**
 * Function: createFile
 * --------------
 * @brief Create the output.csv file and write the header line
 *
 * @return FILE* Opened output file
 *
 */
FILE* createFile(void) {
    FILE* ofp = fopen(OUTPUTFILE, "w");
    if (ofp == NULL) {
        printf("File open error");
        exit(EXIT_FAILURE);
    }
    fputs("Artist(s),Song\n", ofp);
    return (ofp);
}

/**
 * Function: writeOutput
 * --------------
 * @brief Write a line on the output.csv file
 *
 * @param filename The name of the file with write access
 * @param artist Artist name
 * @param song Song title
 * @return nothing
 *
 */
void writeOutput(FILE* filename, char* artist, char* song){
    char str[MAX_LINE_LEN];
    strcpy(str, artist);
    strcat(str, ",");
    strcat(str, song);
    strcat(str, "\n");
    fputs(str, filename);
}

/**
 * Function: stringLoop
 * --------------
 * @brief Loop through a string to check if another string is included in it
 *
 * @param sent A string to loop through
 * @param word A string to find the match
 * @return int 0: word is found; 1: word is not found.
 *
 */
int stringLoop(char* sent, char* word) {
    int sentlen = strlen(sent);
    int wordlen = strlen(word);
    int count = 0;
    while (count < sentlen) {
        if (sent[count] == word[0]) {
            int match = 1;
            for (int i = 1; i < wordlen; i++) {
                if (sent[count+i] == word[i]) {
                    match++;
                }
                if (match == wordlen) {
                    return 0;
                }
            }
        }
        count++;
    }
    return 1;
}

/**
 * Function: question1
 * --------------
 * @brief Answers question 1
 */
void question1(void) {
    // defining variables
    char* to_search = "Rae Spoon";
    char line[MAX_LINE_LEN];
    // opening files
    FILE* ifp = openFile(BEFORE);
    FILE* ofp = createFile();
    fgets(line, MAX_LINE_LEN, ifp); // skip the header
    // loop through lines
    while (fgets(line, MAX_LINE_LEN, ifp) != NULL){
        char* token = strtok(line, ",");
        int count = 0;
        // tokenizing loop
        while (token != NULL && count < FIELDS) {
            if (count == ARTIST && strcmp (token, to_search)== 0) {
                writeOutput(ofp, token, line); // write output
            }
            count++;
            token = strtok(NULL, ",");
        }
    }
    fclose(ifp);
    fclose(ofp);
}

/**
 * Function: question2
 * --------------
 * @brief Answers question 2
 */
void question2 (void) {
    // defining variables
    char* to_search = "Tate McRae";
    char line[MAX_LINE_LEN];
    // opening files
    FILE* ifp = openFile(DURING);
    FILE* ofp = createFile();
    fgets(line, MAX_LINE_LEN, ifp); // skip the header
    // loop through lines
    while (fgets(line, MAX_LINE_LEN, ifp) != NULL){
        char* token = strtok(line, ",");
        int count = 0;
        // tokenizing loop
        while (token != NULL && count < FIELDS) {
            if (count == ARTIST && strcmp (token, to_search)== 0) {
                writeOutput(ofp, token, line); // write output
            }
            count++;
            token = strtok(NULL, ",");
        }
    }
    fclose(ifp);
    fclose(ofp);
}

/**
 * Function: question3
 * --------------
 * @brief Answers question 3
 */
void question3(void) {
    // defining variables
    char* to_search = "The Weeknd";
    char* to_search2 = "Major\n";
    char line[MAX_LINE_LEN];
    char song[MAX_LINE_LEN];
    char artist[MAX_LINE_LEN];
    // opening files
    FILE* ifp = openFile(BEFORE);
    FILE* ofp = createFile();
    fgets(line, MAX_LINE_LEN, ifp); // skip the header
    // loop through lines
    while (fgets(line, MAX_LINE_LEN, ifp) != NULL){
        char* token = strtok(line, ",");
        int count = 0;
        int boolean = 1;
        // tokenizing loop
        while (token != NULL && count < FIELDS) {
            if (count == TITLE) {
                strcpy(song, token); // save title
            }
            if (count == ARTIST) {
                strcpy(artist, token); // save artist
                if (strcmp(token, to_search)== 0) {
                    boolean = 0; // mark artist correct
                }
            }
            if (count == SCALE && strcmp(token, to_search2) == 0) {
                if (boolean == 0) { // if condition 1 met
                    writeOutput(ofp, artist, song); // write output
                }
            }
            count++;
            token = strtok(NULL, ",");
        }
    }
    fclose(ifp);
    fclose(ofp);
}

/**
 * Function: question4
 * --------------
 * @brief Answers question 4
 */
void question4(void) {
    // defining variables
    int to_search = 5000;
    char* to_search2 = "D";
    char* to_search3 = "A";
    char line[MAX_LINE_LEN];
    char song[MAX_LINE_LEN];
    char artist[MAX_LINE_LEN];
    // opening files
    FILE* ifp = openFile(DURING);
    FILE* ofp = createFile();
    fgets(line, MAX_LINE_LEN, ifp); //skip the header
    // loop through lines
    while (fgets(line, MAX_LINE_LEN, ifp) != NULL){
        char* token = strtok(line, ",");
        int count = 0;
        int boolean = 1;
        // tokenizing loop
        while (token != NULL && count < FIELDS) {
            if (count == TITLE) {
                strcpy(song, token); // save title
            }
            if (count == ARTIST) {
                strcpy(artist, token); //save artist name
            }
            if (count == PLAYLIST) {
                int streaming = atoi(token);
                if (streaming > to_search) {
                    boolean = 0; // mark that playlist numbers are over 5000
                }
            }
            if (count == KEY && ((strcmp(token, to_search2) == 0) || (strcmp(token, to_search3) == 0))) {
                if (boolean == 0) { // if condition 1 met
                    writeOutput(ofp, artist, song); // add to output file
                }
            }
            count++;
            token = strtok(NULL, ","); //move onto next token
        }
    }
    fclose(ifp);
    fclose(ofp);
}

/**
 * Function: question5
 * --------------
 * @brief Answers question 5
 */
void question5(void) {
    // defining variables
    int to_search = 2021;
    int to_search2 = 2022;
    char* to_search3 = "Drake";
    char line[MAX_LINE_LEN];
    char song[MAX_LINE_LEN];
    char artist[MAX_LINE_LEN];
    //open files
    FILE* ifp = openFile(DURING);
    FILE* ofp = createFile();
    fgets(line, MAX_LINE_LEN, ifp); //skip the header
    // loop through lines
    while (fgets(line, MAX_LINE_LEN, ifp) != NULL){
        char* token = strtok(line, ",");
        int count = 0;
        int boolean = 1;
        // tokenizing loop
        while (token != NULL && count < FIELDS) {
            if (count == TITLE) {
                strcpy(song, token); // save title
            }
            if (count == ARTIST) {
                strcpy(artist, token); //save artist name
                if (stringLoop(token, to_search3) == 0) {
                    boolean = 0; // mark artist included
                }
            }
            if (count == YEAR) {
                int release_year = atoi(token);
                if (release_year == to_search|| release_year == to_search2) {
                    if (boolean == 0) { // if condition 1 met
                        writeOutput(ofp, artist, song); // add to output file
                    }
                }
            }
            count++;
            token = strtok(NULL, ","); //move onto next token
        }
    }
    fclose(ifp);
    fclose(ofp);
}