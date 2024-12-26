package Interfaces;

import Abstracts.HumanAbstract;
import Abstracts.PlaceAbstract;

public interface Job {
    void doJob(HumanAbstract human, PlaceAbstract place);
}